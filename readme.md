# Mixing an audio file with a noise file at specific Signal-to-Noise Ratio

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

## Usage
Example: `python3 create_noisy_minumum_code.py --clean_file ~/Desktop/test_source/arctic_b0001.wav --noise_file ~/Desktop/test_noise/0ch01.wav --output_clean_file ~/Desktop/clean.wav --output_noise_file ~/Desktop/noise.wav  --output_noisy_file ~/Desktop/noisy.wav --snr 0`

## Dataset
[Voices](http://festvox.org/cmu_arctic/)
[Noises](https://zenodo.org/record/1227121#.W2wUVNj7TUI)
