
import numpy as np
import matplotlib.pyplot as plt

def generate_sin(freq, duration, srate=44100.0, amp=1.5,phase=0):
    t = numpy.linspace(0,duration,int(srate*duration))
    data = amp * numpy.sin(2*numpy.pi*freq *t + phase)
    return data

data_unit = generate_sin(freq, 0.5, amp)
data_f2 = generate_sin(freq, 0.5, amp*2)


data = np.array([])
nv = np.arange(-N/2, N/2)
kv = np.arange(-N/2, N/2)

#for k in range(N):
#    s = np.exp(1j * 2 * np.pi * k / N * np.arange(N))
#    X = np.append(X, sum(x*np.conjugate(s)))
for k in kv:
    s = np.exp(1j * 2 * np.pi * k / N * nv)
    X = np.append(X, sum(x*np.conjugate(s)))

y = np.array([])
for n in nv:
    s = np.exp(1j * 2 * np.pi * n / N * kv)
    y = np.append(y, 1.0/N * sum(X*s))


#plt.plot(np.arange(N), abs(X))
#plt.axis([0, N-1, 0, N])
plt.plot(kv, abs(X))
plt.axis([-N/2, N/2-1, 0, N])

plt.show()
