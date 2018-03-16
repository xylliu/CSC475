import numpy as np
import scipy.io.wavfile as sc
import scipy.fftpack as fft
import matplotlib.pyplot as plt

def spectral_centroid(x, samplerate=44100):
    magnitudes = np.abs(np.fft.rfft(x))
    length = len(x)
    freqs = np.abs(np.fft.fftfreq(length, 1.0/samplerate)[:length//2+1])
    return np.sum(magnitudes*freqs) / np.sum(magnitudes)
sr = 44100
rate, data = sc.read('qbhexamples.wav')
count = 0
maxN = []
chunkF = []
nframe = len(data)
while count < nframe / 2048:
        for x in range(2048):
                if x + count * 2048 < nframe:
                        if data[x + count * 2048] < 0:
                                chunkF.append(0)
                        else:
                                chunkF.append(data[x + count * 2048])
        maxN.append(spectral_centroid(chunkF, sr))
        count += 1
        del chunkF[:]

plt.figure()
plt.plot(range(0, len(maxN)), maxN)
plt.savefig('q2_1_3.png')

def generate_sin(freq, duration, srate=44100.0, amp=1.0,phase=0):
    t = np.linspace(0,duration,int(srate*duration))
    data = amp * np.sin(2*np.pi*freq *t + phase)
    return data

freq = 440
srate = 44100
duration = 5
amp = 2.0
phase = 5
time_space = np.linspace(0, 1000/44100,1000)
data = amp *np.sin(2*np.pi*freq*time_space+phase)
audio_file = wave.open('result.wav', 'w')
audio_file.setparams((1, 2, 44100, 1000, "NONE", "Uncompressed"))
for i in data:
    packed_value = struct.pack('h', np.int16(i))
    audio_file.writeframes(packed_value)
audio_file.close()

