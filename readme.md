# Mixing an audio file with a noise file at any Signal-to-Noise Ratio

## Installation
- Python3.5
- MacOS

### Library
- argparse
- array
- math
- numpy
- random
- wave

### File format
To use this code, the format of source waveforms is as follows.

- 16-bit PCM
- 1 channel

Additionally, the sampling rate of a clean file and that of noise file are supposed to be the same.

## Usage
Example: `python3 create_mixed_audio_file.py --clean_file data/source_clean/arctic_a0001.wav  --noise_file data/source_noise/ch01.wav --output_mixed_file data/output_mixed/0.wav --snr 0`

## Dataset
- [Voices](http://festvox.org/cmu_arctic/)
- [Noises](https://zenodo.org/record/1227121#.W2wUVNj7TUI)

## Detail
There is the detail on my post (in Japanese).

https://engineering.linecorp.com/ja/blog/voice-waveform-arbitrary-signal-to-noise-ratio-python/

There is the detail on my post (in Korean).

https://engineering.linecorp.com/ko/blog/voice-waveform-arbitrary-signal-to-noise-ratio-python/
