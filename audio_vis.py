import librosa
import librosa.display as dsp
from IPython.display import Audio
import matplotlib.pyplot as plt
import numpy as np

data1, sample_rate = librosa.load('myrecording.wav',duration=60)
Audio(data=data1,rate=sample_rate)

print('For 1st recording file')
print('Total number of samples: ',data1.shape[0])
print('Sample rate: ',sample_rate)
print('Length of file in seconds: ',librosa.get_duration(data1))


fig = plt.plot(figsize=(10,7))
librosa.display.waveshow(data1, sr=sample_rate)
plt.title('Envelope view, Data Recording')
plt.show()



X = librosa.stft(data1)
Xdb = librosa.amplitude_to_db(abs(X))

plt.figure(figsize=(15, 3))
librosa.display.specshow(Xdb, sr=sample_rate, x_axis='time', y_axis='hz')
plt.colorbar()
plt.show()

S, phase = librosa.magphase(librosa.stft(data1))
rms = librosa.feature.rms(S=S)

fig, ax = plt.subplots(figsize=(15, 6), nrows=2, sharex=True)
times = librosa.times_like(rms)
ax[0].semilogy(times, rms[0], label='RMS Energy')
ax[0].set(xticks=[])
ax[0].legend()
ax[0].label_outer()
librosa.display.specshow(librosa.amplitude_to_db(S, ref=np.max),
                         y_axis='log', x_axis='time', ax=ax[1])
ax[1].set(title='log Power spectrogram')
plt.show()

mfccs = librosa.feature.mfcc(data1, sr=sample_rate)

plt.figure(figsize=(15, 3))
librosa.display.specshow(mfccs, sr=sample_rate, x_axis='time')
plt.show()