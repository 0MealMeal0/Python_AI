import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
#https://librosa.org/doc/main/troubleshooting.html
from matplotlib import cm

# 음원에 대한 주파수를 출력하는 소스

audio_path = 'piano_sound/37.wav'
y, sr = librosa.load(audio_path, sr=44100)

# stft_result = librosa.stft(y, n_fft=4096, win_length = 4096, hop_length=512)
# D = np.abs(stft_result)
# S_dB = librosa.power_to_db(D, ref=np.max)
# librosa.display.specshow(S_dB, sr=sr, hop_length = 1024, y_axis='mel', x_axis='time', cmap = cm.jet)
# plt.colorbar(format='%2.0f dB')
# plt.show()

n_fft = 2048
S = librosa.stft(y, n_fft=n_fft, hop_length=n_fft//2)
# convert to db
# (for your CNN you might want to skip this and rather ensure zero mean and unit variance)
D = librosa.amplitude_to_db(np.abs(S), ref=np.max)
# average over file
D_AVG = np.mean(D, axis=1)

plt.bar(np.arange(D_AVG.shape[0]), D_AVG)
x_ticks_positions = [n for n in range(0, n_fft // 2, n_fft // 16)]
x_ticks_labels = [str(sr / 2048 * n) + 'Hz' for n in x_ticks_positions]
plt.xticks(x_ticks_positions, x_ticks_labels)
plt.xlabel('Frequency')
plt.ylabel('dB')
plt.show()
#https://stackoverflow.com/questions/55842277/how-to-plot-spectrum-or-frequency-vs-amplitude-of-entire-audio-file-using-python