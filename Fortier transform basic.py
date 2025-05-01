import numpy as np
#before the function you need to load your signal
def EEG_energy(singal, fs, low_freq, high_freq):
    fft_result = np.fft.fft(singal)
    freqs = np.fft.fftfreq(len(signal), d = 1/fs)
    mask = (freqs >= low_freq) & (freqs <= high_freq)
    energy = np.sum(np.abs(fft_result[mask])**2)
    return energy