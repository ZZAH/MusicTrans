from pathlib import Path
import librosa
import torch
from argparse import ArgumentParser
import matplotlib
import h5py
import tqdm
from IPython.display import Audio, display

import sys
sys.path += ['../src']

import utils
import wavenet_models
from utils import save_audio
from wavenet import WaveNet
from wavenet_generator import WavenetGenerator

from nv_wavenet_generator import NVWavenetGenerator
import numpy as np
import librosa.display
import matplotlib.pyplot as plt
import sys
matplotlib.use('agg')
file_paths = Path('voilins_1.wav')
data, rate = librosa.load(file_paths, sr=1600)
start = 12
duration = 5
stop = start +duration
audio_dst = data[start*160:stop*160]
print(audio_dst.shape)
librosa.display.waveplot(audio_dst, sr=1600)
plt.savefig("piano.png")

plt.figure(figsize=(30, 15))
matplotlib.use('agg')
file_paths = Path('voilins_1.wav')
data, rate = librosa.load(file_paths, sr=1600)
start = 12
duration = 30
stop = start +duration
audio_dst = data[start*1600:stop*1600]
print(audio_dst.shape)
D = librosa.amplitude_to_db(librosa.stft(audio_dst), ref=np.max)
plt.subplot(4, 2, 1)
librosa.display.specshow(D, sr=1600, hop_length=32,y_axis='linear')
plt.savefig("piano_fimg1600.png")


zero_crossing_rate = librosa.feature.zero_crossing_rate(audio_dst,hop_length=)
print("tempogram:", librosa.feature.tempogram(audio_dst, sr=1600))32
print("zero_cross: ", zero_crossing_rate)
