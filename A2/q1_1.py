import numpy as np
import scipy.io.wavfile as sc
import matplotlib.pyplot as plt
from scipy.fftpack import fft
import math
import wave

rate, a = sc.read("output.wav")
rate, b = sc.read("Ah.wav")
rate, c = sc.read("qbhexamples.wav")

types = {1: np.int8, 2: np.int16, 4: np.int32}

s = 2048
sr = 44100
window = np.hamming(2048)

wave_a = wave.open('output.wav')
#nframe_a = wave_a.getnframes()
a_nchannels, a_sampwidth, a_framerate, a_nframes, a_comptype, a_compname = wave_a.getparams()

wave_b = wave.open('Ah.wav')
#nframe_a = wave_a.getnframes()
b_nchannels, b_sampwidth, b_framerate, b_nframes, b_comptype, b_compname = wave_b.getparams()

wave_c = wave.open('qbhexamples.wav')
#nframe_a = wave_a.getnframes()
c_nchannels, c_sampwidth, c_framerate, c_nframes, c_comptype, c_compname = wave_c.getparams()

fft_aout = abs(fft(a))
fft_bout = abs(fft(b))
fft_cout = abs(fft(c))

freqa = []
freqb = []
freqc = []

for i in range(a_nframes // s):
    content_a = wave_a.readframes(s)
    sam = np.fromstring(content_a, dtype=types[a_sampwidth])[0::a_nchannels]
    sam = sam * window
    fft_aout = abs(fft(sam,2048))
    fund_freq_a = sr * np.argmax(fft_aout) / len(fft_aout)
    plt.figure()
    freqa.append(fund_freq_a)
    plt.plot(freqa)
    plt.savefig("nq1_1A.png")

for i in range(b_nframes // s):
    content_b = wave_b.readframes(s)
    sbm = np.fromstring(content_b, dtype=types[b_sampwidth])[0::b_nchannels]
    sbm = sbm * window
    fft_bout = abs(fft(sbm,2048))
    fund_freq_b = sr * np.argmax(fft_bout) / len(fft_bout)
    freqb.append(fund_freq_b)
    plt.figure()
    plt.plot(freqb)
    plt.savefig("nq1_1B.png")

for i in range(c_nframes // s):
    content_c = wave_c.readframes(s)
    scm = np.fromstring(content_c, dtype=types[c_sampwidth])[0::c_nchannels]
    scm = scm * window
    fft_cout = abs(fft(scm,2048))
    fund_freq_c = sr * np.argmax(fft_cout) / len(fft_cout)
    freqc.append(fund_freq_c)
    plt.figure()
    plt.plot(freqc)
    plt.savefig("nq1_1C.png")

