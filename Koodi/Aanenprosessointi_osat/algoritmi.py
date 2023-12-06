import scipy.fftpack as fft

import numpy as np


def _FFT(data):
    '''
    FFT : Fast Fourier Transform : Nopea Fourier-Muunnos

    Muuttujat:
    data = Syöte taulukko # Taulukon pituus tulee olla muotoa 2^n, jotta algoritmi toimii oikein
    
    Palauttaa Fourier-muunnetun data taulukon  
    '''

    pituus = len(data)
    

    if pituus == 1:
        return data
    else:
        parilliset = _FFT(data[::2])
        parittomat = _FFT(data[1::2])

        yksikkojuuret = np.exp(-2j*np.pi*np.arange(pituus)/ pituus)
        yksikkojuuretJaettu=np.array_split(yksikkojuuret, 2)

        muunnos = np.concatenate([parilliset+yksikkojuuretJaettu[0]*parittomat, parilliset+yksikkojuuretJaettu[1]*parittomat])
        
        return muunnos
    
def _iFFT(data):
    '''
    iFFT : inverse Fast Fourier Transform : käänteinen Nopea Fourier-Muunnos

    Muuttujat:
    data = Syöte taulukko
    
    Palauttaa käänteisesti Fourier-muunnetun data taulukon  
    '''

    pituus = len(data)
    

    if pituus == 1:
        return data
    else:
        parilliset = _iFFT(data[::2])
        parittomat = _iFFT(data[1::2])

        yksikkojuuret = np.exp(2j*np.pi*np.arange(pituus)/ pituus)
        yksikkojuuretJaettu=np.array_split(yksikkojuuret, 2)

        muunnos = np.concatenate([parilliset+yksikkojuuretJaettu[0]*parittomat, parilliset+yksikkojuuretJaettu[1]*parittomat])
        
        return muunnos

def suorita_FFT_datalle(data, omaFFTtoteutus=True):
    if omaFFTtoteutus:
        muunnos = _FFT(data)
    else:
        muunnos = fft.fft(data)

    return muunnos

def suorita_iFFT_datalle(data, omaFFTtoteutus=True):
    if omaFFTtoteutus:
        muunnos = _FFT(data)
    else:
        muunnos = fft.fft(data)

    return muunnos
