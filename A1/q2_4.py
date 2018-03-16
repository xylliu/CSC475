from pylab import *
import sympy
import wave
import struct
import numpy

buffer_size = 2048
audio_file = wave.open('0_phase.wav', 'r')
#audio_file = wave.open('/home/hoverbear/test.wav', 'r')
out_file = wave.open('q2_4.wav', 'w')

out_file.setparams(audio_file.getparams())
num_of_frames = buffer_size / (audio_file.getsampwidth() + audio_file.getnchannels())

while True:
    frames = audio_file.readframes(int(num_of_frames))
    if not frames:
        break
    working_set = numpy.fromstring(frames, numpy.int16)
    fft_set = fft(working_set) / len(working_set)

    for i in range(0, len(fft_set)):
        fft_set[i] = (fft_set[i].real) + (fft_set[i].imag + numpy.random.random() * 1000)*1j

    inverse_fft_set = ifft(fft_set) * len(working_set)
    plt.figure()
    plt.plot(range(0, len(inverse_fft_set)), [i.real for i in inverse_fft_set])
    plt.plot(range(0, len(inverse_fft_set)), [i.imag for i in inverse_fft_set])
    show()
    for i in inverse_fft_set:
        packed_value = struct.pack('h', int16(i.real))
        out_file.writeframes(packed_value)

out_file.close()
