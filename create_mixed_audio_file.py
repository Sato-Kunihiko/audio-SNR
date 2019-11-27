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
    parser.add_argument('--output_mixed_file', type=str, default='', required=True)
    parser.add_argument('--output_clean_file', type=str, default='')
    parser.add_argument('--output_noise_file', type=str, default='')
    parser.add_argument('--snr', type=float, default='', required=True)
    args = parser.parse_args()
    return args

def cal_adjusted_rms(clean_rms, snr):
    a = float(snr) / 20
    noise_rms = clean_rms / (10**a) 
    return noise_rms

def cal_amp(wf):
    buffer = wf.readframes(wf.getnframes())
    # The dtype depends on the value of pulse-code modulation. The int16 is set for 16-bit PCM.
    amptitude = (np.frombuffer(buffer, dtype="int16")).astype(np.float64)
    return amptitude

def cal_rms(amp):
    return np.sqrt(np.mean(np.square(amp), axis=-1))

def save_waveform(output_path, params, amp):
    output_file = wave.Wave_write(output_path)
    output_file.setparams(params) #nchannels, sampwidth, framerate, nframes, comptype, compname
    output_file.writeframes(array.array('h', amp.astype(np.int16)).tobytes() )
    output_file.close()

if __name__ == '__main__':
    args = get_args()

    clean_file = args.clean_file
    noise_file = args.noise_file

    clean_wav = wave.open(clean_file, "r")
    noise_wav = wave.open(noise_file, "r")

    clean_amp = cal_amp(clean_wav)
    noise_amp = cal_amp(noise_wav)

    clean_rms = cal_rms(clean_amp)

    start = random.randint(0, len(noise_amp)-len(clean_amp))
    divided_noise_amp = noise_amp[start: start + len(clean_amp)]
    noise_rms = cal_rms(divided_noise_amp)

    snr = args.snr
    adjusted_noise_rms = cal_adjusted_rms(clean_rms, snr)
    
    adjusted_noise_amp = divided_noise_amp * (adjusted_noise_rms / noise_rms) 
    mixed_amp = (clean_amp + adjusted_noise_amp)

    #Avoid clipping noise
    max_int16 = np.iinfo(np.int16).max
    min_int16 = np.iinfo(np.int16).min
    if mixed_amp.max(axis=0) > max_int16 or mixed_amp.min(axis=0) < min_int16:
        if mixed_amp.max(axis=0) >= abs(mixed_amp.min(axis=0)): 
            reduction_rate = max_int16 / mixed_amp.max(axis=0)
        else :
            reduction_rate = min_int16 / mixed_amp.min(axis=0)
        mixed_amp = mixed_amp * (reduction_rate)
        clean_amp = clean_amp * (reduction_rate)

    save_waveform(args.output_mixed_file, clean_wav.getparams(), mixed_amp)
