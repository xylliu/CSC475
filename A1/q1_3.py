import matplotlib
matplotlib.use('AGG')
import matplotlib.pyplot as plt
import numpy as np
import random
import wave
import struct


def generate_sin(freq, duration=1 , srate=44100.0, amp=1.0,phase=0):
    t = np.linspace(0,duration,int(srate*duration))
    data = amp * np.sin(2*np.pi*freq *t + phase)
    return data

freq = 440
srate = 44100
time_space = np.linspace(0, 1000/44100, 1000)

#generating phase = 0
data_f1 = generate_sin(freq, amp=1.0)
data_f2 = generate_sin(freq*3, amp = 0.5)
data_f3 = generate_sin(freq*4, amp = 0.33)

data = [data_f1[i] + data_f2[i] + data_f3[i] for i in range(0, len(data_f1))]

audio_file = wave.open('0_phase.wav', 'w')
audio_file.setparams((1, 2, 44100, 1000, "NONE", "Uncompressed"))
for i in data:
    packed_value = struct.pack('h', np.int16(i))
    audio_file.writeframes(packed_value)
audio_file.close()

#0 phase plot
plt.figure()
plt.plot(time_space[0:1000] * srate, data[0:1000]);
fname='q1_3_0_phase.png'
plt.savefig(fname)

#random phase
data_f4 = generate_sin(freq, amp=1.0,phase=random.random())
data_f5 = generate_sin(freq*3, amp = 0.5,phase=random.random())
data_f6 = generate_sin(freq*4, amp = 0.33,phase=random.random())
data2 = [data_f4[i] + data_f5[i] + data_f6[i] for i in range(0, len(data_f4))]

audio_file = wave.open('random_phase.wav', 'w')
audio_file.setparams((1, 2, 44100, 1000, "NONE", "Uncompressed"))
for i in data2:
    packed_value = struct.pack('h', np.int16(i))
    audio_file.writeframes(packed_value)
audio_file.close()

#random phase plot
plt.figure()
plt.plot(time_space[0:1000] * srate, data2[0:1000]);
fname='q1_3_random_phase.png'
plt.savefig(fname)

#plot 3 input sinusoid
plt.figure()
plt.plot(time_space[0:1000] * srate, data_f1[0:1000]);
plt.plot(time_space[0:1000] * srate, data_f2[0:1000]);
plt.plot(time_space[0:1000] * srate, data_f3[0:1000]);
fname='q1_3_input.png'
plt.savefig(fname)
