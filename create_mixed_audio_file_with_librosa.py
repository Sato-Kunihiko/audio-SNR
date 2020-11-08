# -*- coding: utf-8 -*-
import argparse
import array
import librosa
import math
import numpy as np
import random
import soundfile as sf
from enum import Enum

class EncodingType(Enum):
    def __new__(cls, *args, **kwds):
        value = len(cls.__members__) + 4
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __init__(self, dtype, desc, subtype, maximum, minimum):
        self.dtype = dtype
        self.desc = desc
        self.subtype = subtype
        self.maximum = maximum
        self.minimum = minimum

    # TODO: Attach link for dtype and subtype in soundfile
    INT16 = "int16", "Signed 16 bit PCM", "PCM_16", np.iinfo(np.int16).max, np.iinfo(np.int16).min
    FLOAT64 = "float64", "64 bit float",  "DOUBLE", np.finfo(np.float64).max, np.finfo(np.float64).min


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--clean_file", type=str, required=True)
    parser.add_argument("--noise_file", type=str, required=True)
    parser.add_argument("--output_mixed_file", type=str, default="", required=True)
    parser.add_argument("--output_clean_file", type=str, default="")
    parser.add_argument("--output_noise_file", type=str, default="")
    parser.add_argument("--snr", type=float, default="", required=True)
    args = parser.parse_args()
    return args


def cal_adjusted_rms(clean_rms, snr):
    a = float(snr) / 20
    noise_rms = clean_rms / (10 ** a)
    return noise_rms


def cal_rms(amp):
    return np.sqrt(np.mean(np.square(amp), axis=-1))


def save_waveform(output_path, amp, samplerate, subtype):
    sf.write(output_path, amp, samplerate, subtype=subtype)
    metadata = sf.info(output_path)
    print(metadata)
    print(amp)


if __name__ == "__main__":
    args = get_args()

    clean_file = args.clean_file
    noise_file = args.noise_file

    metadata = sf.info(clean_file)
    for item in EncodingType:
        if item.desc == metadata.subtype_info:
            encoding_type = item


    # Set float64 to dtype to hadle amplitude value with various encoding method (16-bit Signed Integer PCM, 32-bit float, 64-bit float, etc...)
    clean_amp, clean_samplerate = sf.read(clean_file, dtype=encoding_type.dtype)
    noise_amp, noise_samplerate = sf.read(noise_file, dtype=encoding_type.dtype)
    print(clean_amp[1000:1100])

    clean_rms = cal_rms(clean_amp)

    start = random.randint(0, len(noise_amp) - len(clean_amp))
    divided_noise_amp = noise_amp[start : start + len(clean_amp)]
    noise_rms = cal_rms(divided_noise_amp)

    snr = args.snr
    adjusted_noise_rms = cal_adjusted_rms(clean_rms, snr)

    adjusted_noise_amp = divided_noise_amp * (adjusted_noise_rms / noise_rms)
    mixed_amp = clean_amp + adjusted_noise_amp
    print(mixed_amp.max(axis=0))

    # Avoid clipping noise
    max_limit = encoding_type.maximum
    min_limit = encoding_type.minimum
    print(max_limit, min_limit)
    if mixed_amp.max(axis=0) > max_limit or mixed_amp.min(axis=0) < min_limit:
        print("over!")
        if mixed_amp.max(axis=0) >= abs(mixed_amp.min(axis=0)):
            reduction_rate = max_limit / mixed_amp.max(axis=0)
        else:
            reduction_rate = min_limit / mixed_amp.min(axis=0)
        mixed_amp = mixed_amp * (reduction_rate)
        clean_amp = clean_amp * (reduction_rate)

    save_waveform(args.output_mixed_file, mixed_amp, clean_samplerate, encoding_type.subtype)
