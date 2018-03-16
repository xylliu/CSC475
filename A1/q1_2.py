import matplotlib
matplotlib.use('AGG')

import matplotlib.pyplot as plt
from pylab import *
import numpy as np
import random

def generate_sin(freq, duration, srate=44100.0, amp=1.0,phase=0): 
    t = np.linspace(0,duration,int(srate*duration))
    data = amp * np.sin(2*np.pi*freq *t + phase)
    return data

freq = 440
srate = 44100
time_space = np.linspace(0, 1000/44100,1000)

#generating three sin wave by different frequency and different phase
data_f1 = generate_sin(freq, 0.5, amp=1.0)
data_f2 = generate_sin(freq*2, 0.5, amp = 0.5)
data_f3 = generate_sin(freq*3, 0.5, amp = 0.33)

#mixture of three harmonically related sinusoids
data = [data_f1[i] + data_f2[i] + data_f3[i] for i in range(0, len(data_f1))]

#saving time domain plot in a pdf file
plt.figure()
plt.plot(time_space[0:1000] * srate, data[0:1000]);
fname='0phase.pdf'
plt.savefig(fname)

#generating three sin wave by different frequency and random phase
data_f4 = generate_sin(freq, 0.5, amp=1.0,phase=random.random())
data_f5 = generate_sin(freq*2, 0.5, amp = 0.5,phase=random.random())
data_f6 = generate_sin(freq*3, 0.5, amp = 0.33,phase=random.random())

data2 = [data_f4[i] + data_f5[i] + data_f6[i] for i in range(0, len(data_f4))]

plt.figure()
plt.plot(time_space[0:1000] * srate, data2[0:1000]);
fname='random_phase.pdf'
plt.savefig(fname)
