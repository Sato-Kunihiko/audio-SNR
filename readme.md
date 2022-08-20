# Mixing an audio file with a noise file at any Signal-to-Noise Ratio
The script `create_mixed_audio_file.py` and `create_mixed_audio_file_with_soundfile.py` can mix an audio file with a noise file at any Signal-to-Noise Ratio (SNR). 

You can listen to the results of [mixtures](/data/16_bit/output_mixed) of the [clean voice](data/16_bit/source_clean) and the [noise](data/16_bit/source_noise).

## Installation
- Python3.7+
- macOS

### Setup
I recommend to install [Pipenv](https://github.com/pypa/pipenv) for making set-up easy before proceeding:

If you're on macOS, you can install Pipenv easily with Homebrew:

```
$ brew install pipenv
```

After installing Pipenv, you run the following command to build a virtualenv and install packages listed in `Pipfile.lock`.

```
$ pipenv install
```

Then, you can run the following command to activate a virtualenv.

```
$ pipenv shell
```

### File format
To use this code, the format of source waveforms is as follows.

- WAV file
- 1 channel

Additionally, the sampling rate of a clean file and that of a noise file are supposed to be the same.

## Usage
There are two files for creating a mixture.

- `create_mixed_audio_file.py`:
  - Uses wave module
  - Can read wav file with 16-bit PCM only

- `create_mixed_audio_file_with_soundfile.py`:
  - Uses soundfile library
  - Can read wav file with various encoding types such as 16-bit PCM, 32-bit PCM, 32-bit float, and 64-bit float. 

After activating a virtualenv, you can run the files to mix an audio file with a noise file at any signal-to-noise ratio.

Example of `create_mixed_audio_file.py`: 

```
python create_mixed_audio_file.py --clean_file ~/workspace/audio-SNR/data/16_bit/source_clean/arctic_a0001.wav --noise_file ~/workspace/audio-SNR/data/16_bit/source_noise/ch01.wav --snr 0 --output_mixed_file ~/workspace/audio-SNR/data/16_bit/output_mixed/0dB.wav
```

Example of `create_mixed_audio_file_with_soundfile.py`:

```
python create_mixed_audio_file_with_soundfile.py --clean_file ~/workspace/audio-SNR/data/64_bit/source_clean/arctic_a0001_64bit.wav --noise_file ~/workspace/audio-SNR/data/64_bit/source_noise/ch01_64bit.wav --snr 0 --output_mixed_file ~/workspace/audio-SNR/data/64_bit/output_mixed/0dB.wav
```

## Dataset
I really appreciate the following public datasets.

- [Voices](http://festvox.org/cmu_arctic/) - CMU_ARCTIC speech synthesis databases
- [Noises](https://zenodo.org/record/1227121#.W2wUVNj7TUI) - DEMAND: a collection of multi-channel recordings of acoustic noise in diverse environments

## Detail
There is a detail about `create_mixed_audio_file.py` on my post (in Japanese).

[https://engineering.linecorp.com/ja/blog/voice-waveform-arbitrary-signal-to-noise-ratio-python/](https://engineering.linecorp.com/ja/blog/voice-waveform-arbitrary-signal-to-noise-ratio-python/)

There is a detail about `create_mixed_audio_file.py` on my post (in Korean).

[https://engineering.linecorp.com/ko/blog/voice-waveform-arbitrary-signal-to-noise-ratio-python/](https://engineering.linecorp.com/ko/blog/voice-waveform-arbitrary-signal-to-noise-ratio-python/)