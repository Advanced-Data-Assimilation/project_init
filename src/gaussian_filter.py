import numpy as np
from scipy.fft import fft, ifft


def gaussian_filter(f, g, weight_corr):
    # FFT Convolution
    f_ij = fft(fft(f, axis=0), axis=1)
    g_ij = fft(fft(g, axis=0), axis=1)
    
    # Corr
    f_convolv_g = ifft(ifft(f_ij * g_ij[:, :, np.newaxis], axis=0), axis=1) @ weight_corr

    return f_convolv_g