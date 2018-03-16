from numpy import array,matrix,pi,exp,sin,linspace,log10
from numpy.fft import fft
import matplotlib.pyplot as plt

i=1j
def dft(X):
    N = len(X)
    w = exp(-2*pi*i/N)
    A = array([ [w**(j*k) for j in range(0,N) ] for k in range(0,N) ])
    Y = A.dot(X)
    return Y

def f(x): return sin(x)

X = linspace(0.01,2*pi,100)
f_X = f(X)
dft_X = dft(f_X)
fft_X = fft(f_X)

fig = plt.figure()
ax1 = fig.add_subplot(231)
ax1.plot(dft_X,label="DFT")
ax1.legend()
ax2 = fig.add_subplot(232)
ax2.plot(fft_X,label="FFT")
ax2.legend()
plt.savefig("fft_vs_dft.png")
