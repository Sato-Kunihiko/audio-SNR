# -*- coding: utf-8 -*-
import argparse
import array
import math
import numpy as np
import random
import wave

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean_file', type=str, required=True)
    parser.add_argument('--noise_file', type=str, required=True)
    parser.add_argument('--output_clean_file', type=str, default='')
    parser.add_argument('--output_noise_file', type=str, default='')
    parser.add_argument('--output_noisy_file', type=str, default='', required=True)
    parser.add_argument('--snr', type=float, default='', required=True)
    args = parser.parse_args()
    return args

def cal_adjusted_rms(clean_rms, snr):
    a = float(snr) / 20
    noise_rms = clean_rms / (10**a) 
    return noise_rms

def cal_amp(wf):
    buffer = wf.readframes(wf.getnframes())
    amptitude = (np.frombuffer(buffer, dtype="int16")).astype(np.float64)
    return amptitude

def cal_rms(amp):
    return np.sqrt(np.mean(np.square(amp), axis=-1))

if __name__ == '__main__':
    args = get_args()

    clean_file = args.clean_file
    noise_file = args.noise_file
    snr = args.snr

    clean_wav = wave.open(clean_file, "r")
    noise_wav = wave.open(noise_file, "r")

    clean_amp = cal_amp(clean_wav)
    noise_amp = cal_amp(noise_wav)

    start = random.randint(0, len(noise_amp)-len(clean_amp))
    clean_rms = cal_rms(clean_amp)
    split_noise_amp = noise_amp[start: start + len(clean_amp)]
    noise_rms = cal_rms(split_noise_amp)

    adjusted_noise_rms = cal_adjusted_rms(clean_rms, snr)
    
    adjusted_noise_amp = split_noise_amp * (adjusted_noise_rms / noise_rms) 
    mixed_amp = (clean_amp + adjusted_noise_amp)

    if (mixed_amp.max(axis=0) > 32767): 
        mixed_amp = mixed_amp * (32767/mixed_amp.max(axis=0))
        clean_amp = clean_amp * (32767/mixed_amp.max(axis=0))
        adjusted_noise_amp = adjusted_noise_amp * (32767/mixed_amp.max(axis=0))

    noisy_wave = wave.Wave_write(args.output_noisy_file)
    noisy_wave.setparams(clean_wav.getparams())
    noisy_wave.writeframes(array.array('h', mixed_amp.astype(np.int16)).tostring() )
    noisy_wave.close()

    clean_wave = wave.Wave_write(args.output_clean_file)
    clean_wave.setparams(clean_wav.getparams())
    clean_wave.writeframes(array.array('h', clean_amp.astype(np.int16)).tostring() )
    clean_wave.close()

    noise_wave = wave.Wave_write(args.output_noise_file)
    noise_wave.setparams(clean_wav.getparams())
    noise_wave.writeframes(array.array('h', adjusted_noise_amp.astype(np.int16)).tostring() )
    noise_wave.close()
