# Beat tracking example
# from __future__ import print_function
import librosa
import numpy as np
import matplotlib.pyplot as plt

# 1. Get the file path to the included audio example
# filename = librosa.util.example_audio_file()

# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load('test.wav')

# sp = np.abs(np.fft.fft(y))**2
# sp1 = sp[50:500]
# gr = np.gradient(sp1)

# y_harmonic, y_percussive = librosa.effects.hpss(y, margin=(1.0,5.0))

# # 3. Run the default beat tracker
# tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#
# print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
#
# # 4. Convert the frame indices of beat events into timestamps
# beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#
# print('Saving output to beat_times.csv')
# librosa.output.times_csv('beat_times.csv', beat_times)

sf = librosa.feature.spectral_flatness(y)
sc = librosa.feature.spectral_centroid(y)

print(sf.size)

# plt.plot(y)
# plt.plot(sf)
# plt.plot(gr)
# plt.plot(y_harmonic)
# plt.plot(y_percussive)
plt.plot(sc)
plt.show()