import matplotlib.pyplot as plt
import sympy
import wave
import struct
import numpy as np

srate = 44100
time_space = np.linspace(0, 2, 2*44100)
signal_power = 1

def generate_create(noise_db, freq = 440):
    # generating sign wave
    signal_wave = signal_power * np.sin(2 * np.pi * freq * time_space)

    # generating Noise.
    p_noise, p_signal, snr = sympy.symbols("p_noise, p_signal, snr")
    noise_power = sympy.solve(sympy.Eq(10 * sympy.log(p_signal / p_noise, 10), snr), p_noise)[0].evalf(subs = {p_signal: signal_power, snr: noise_db})
    noise_wave = ((np.random.ranf(size = 2*44100) * 2) - 1) * noise_power

    # Create the audio file.
    audio_file = wave.open('q1_6_' + str(noise_db) + '_440Hz.wav', 'w')
    audio_file.setparams((1, 2, srate  , 2*srate , "NONE", "Uncompressed"))
    for i in noise_wave + signal_wave:
        packed_value = struct.pack('h', np.int16(i))
        audio_file.writeframes(packed_value)
    audio_file.close()

generate_create(0)
generate_create(15)
generate_create(-15)
generate_create(10)
generate_create(-10)

def inner_product(data1, data2):
    if len(data1) != len(data2):
        return "cannot do inner product."
    return np.inner(data1, data2)/len(data1)
