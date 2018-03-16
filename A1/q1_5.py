#from pylab import *
import numpy
import wave
import struct
import random
import matplotlib.pyplot as plt


srate = 44100
freq = 440
amp = 1.5

time_space = numpy.linspace(0, 1000/44100, 1000)

phase = 0.0

def inner_product(x, y):
   if len(x) != len(y):
       return "Cannot do innner product"
   return numpy.inner(x,y)/len(x)

def generate_sin(freq, duration, srate=44100.0, amp=1.5,phase=0):
    t = numpy.linspace(0,duration,int(srate*duration))
    data = amp * numpy.sin(2*numpy.pi*freq *t + phase)
    return data

data_unit = generate_sin(freq, 0.5, amp)
data_f2 = generate_sin(freq, 0.5, amp*2)

data = [data_unit[i] + data_f2[i]for i in range(0, len(data_unit))]

# plot(time_space[0:200], mixture[0:200])
plt.figure()
inner_1 = inner_product(data, data_f2)
plt.title('similarity with second unit: ' + str(inner_1))
plt.plot(time_space[0:200]*srate, data[0:200])
plt.plot(time_space[0:200]*srate, data_unit[0:200])
plt.show()
#print("Similar to first wave:", inner_product_1)

data_f3 = generate_sin(freq, 0.5, amp*3)
#data = [data_f1[i] + data_f2[i] for i in range(0, len(data_f1))]
