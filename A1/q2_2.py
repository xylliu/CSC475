import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
from pylab import *
import wave
import struct
import random
import numpy


def generate_sin(freq, duration, srate=44100.0, amp=1.0,phase=0):
    t = np.linspace(0,duration,int(srate*duration))
    data = amp * np.sin(2*np.pi*freq *t + phase)
    return data

freq = 440
srate = 44100
time_space = np.linspace(0, 1000/44100,1000)

#create the three harmonically related sinusoids
data_1 = generate_sin(freq, 0.5, amp=1.0)
data_2 = generate_sin(freq*2, 0.5, amp = 0.5)
data_3 = generate_sin(freq*3, 0.5, amp = 0.33)

data = [data_1[i] + data_2[i] + data_3[i] for i in range(0, len(data_1))]

#plot 0 phase
plt.figure()
plt.plot(time_space[0:1000] * srate, data[0:1000]);
fname='q2_2.pdf'
plt.savefig(fname)

size_fft = len(data)
fft_space = (numpy.fft.fft(data) / size_fft)[0 : int(size_fft / 2)]

plt.figure()
plt.title("Fast Fourier Transform")

size = len(data)
series = arange(size)
intervals = size / srate
frequ= (series / intervals)[0 : int(size / 2)]

plt.plot(frequ, numpy.abs(fft_space))
figurename = 'q2_2m.pdf'
plt.savefig(figurename)
