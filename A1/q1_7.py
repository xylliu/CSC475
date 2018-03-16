import matplotlib.pyplot as plt
import numpy as np
import wave
import struct
import random


srate = 44100
freq = 440

time_space = np.linspace(0, 1000/44100, 1000)

def inner_product(data1, data2):
        if len(data1) != len(data2):
                return "Not allowed to inner product."
        return np.inner(data1, data2)/len(data1)

def generate_sin(freq, duration, srate=44100.0, amp=1.0,phase=0):
    t = np.linspace(0,duration,int(srate*duration))
    data = amp * np.sin(2*np.pi*freq *t + phase)
    return data

data_f1 = generate_sin(freq, 1, amp=1.0)
data_f2 = generate_sin(freq*2, 1, amp = 0.5)
data_f3 = generate_sin(freq*3, 1, amp = 0.33)

data = [data_f1[i] + data_f2[i] + data_f3[i] for i in range(0, len(data_f1))]

data_unit = generate_sin(freq, 1, amp = 1.0)
inner1 = inner_product(data, data_unit)

data_unit2 = generate_sin(freq*2, 1, amp = 1.0)
inner2 = inner_product(data, data_unit2)

plt.figure()
print('inner product of mixture with a unit amplitude sinusoid of frequency f :' + str(inner1))
plt.plot(time_space[0:200]*srate, data[0:200])
plt.plot(time_space[0:200]*srate, data_unit[0:200])
fname = 'q1_7_inner1.pdf'
plt.savefig(fname)

plt.figure()
print('inner product of mixture with a unit amplitude sinusoid of frequency 2f : ' + str(inner2))
plt.plot(time_space[0:200]*srate, data[0:200])
plt.plot(time_space[0:200]*srate, data_unit2[0:200])
fname = 'q1_7_inner2.pdf'
plt.savefig(fname)
