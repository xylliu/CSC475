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

def generate_sin(freq, duration, srate=44100.0, amp=1, phase=0):
    t = np.linspace(0,duration,int(srate*duration))
    data = amp * np.sin(2*np.pi*freq *t + phase)
    return data

data_f1 = generate_sin(freq, 1)
data_f2 = generate_sin(freq, 1, amp = 1.5)
data_f3 = generate_sin(freq, 1, amp = 4.5)

inner_1 = inner_product(data_f1, data_f2)
inner_2 = inner_product(data_f1, data_f3)

print('inner product of two sinusoid with apm = 1.5 and apm = 1: ' + str(inner_1))
print('inner product of two sinusoid with apm = 4.5 and apm = 1: ' + str(inner_2))
