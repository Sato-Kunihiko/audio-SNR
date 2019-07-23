# Mixing an audio file with a noise file at any Signal-to-Noise Ratio

## Installation
- Python3.5+
- MacOS

### Setup
I recommend you install [Pipenv](installation. https://github.com/pypa/pipenv) to make set-up easy before proceeding:

If you're on MacOS, you can install Pipenv easily with Homebrew:

```
$ brew install pipenv
```

After installing pipenv, you run the following command to build a virtualenv and install packages described in Pipfile.lock.

```
$ pipenv install
```

Then, you can run the following command to activate a virtualenv.

```
$ pipenv shell
```

### File format
To use this code, the format of source waveforms is as follows.

- 16-bit PCM
- 1 channel

Additionally, the sampling rate of a clean file and that of noise file are supposed to be the same.

## Usage
After activating a virtualenv, you can run the `create_mixed_audio_file.py` to mix an audio file with a noise file at any signal-to-noise ratio.

Example: 

```
python3 create_mixed_audio_file.py --clean_file data/source_clean/arctic_a0001.wav  --noise_file data/source_noise/ch01.wav --output_mixed_file data/output_mixed/0.wav --snr 0
```

## Dataset
Thank you for open datasets.

- [Voices](http://festvox.org/cmu_arctic/) - CMU_ARCTIC speech synthesis databases
- [Noises](https://zenodo.org/record/1227121#.W2wUVNj7TUI) - DEMAND: a collection of multi-channel recordings of acoustic noise in diverse environments

## Detail
There is the detail on my post (in Japanese).

[https://engineering.linecorp.com/ja/blog/voice-waveform-arbitrary-signal-to-noise-ratio-python/](https://engineering.linecorp.com/ja/blog/voice-waveform-arbitrary-signal-to-noise-ratio-python/)

There is the detail on my post (in Korean).

[https://engineering.linecorp.com/ko/blog/voice-waveform-arbitrary-signal-to-noise-ratio-python/](https://engineering.linecorp.com/ko/blog/voice-waveform-arbitrary-signal-to-noise-ratio-python/)
