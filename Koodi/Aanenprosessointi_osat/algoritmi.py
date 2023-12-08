import scipy.fftpack as fft

import numpy as np


def _fft(data):
    """
    FFT : Fast Fourier Transform : Nopea Fourier-Muunnos

    Muuttujat:
    data = Syöte taulukko # Taulukon pituus tulee olla muotoa 2^n, jotta algoritmi toimii oikein

    Palauttaa Fourier-muunnetun data taulukon
    """

    pituus = len(data)

    if pituus == 1:
        return data

    parilliset = _fft(data[::2])
    parittomat = _fft(data[1::2])

    yksikkojuuret = np.exp(-2j * np.pi * np.arange(pituus) / pituus)
    yksikkojuuretJaettu = np.array_split(yksikkojuuret, 2)

    muunnos = np.concatenate(
        [
            parilliset + yksikkojuuretJaettu[0] * parittomat,
            parilliset + yksikkojuuretJaettu[1] * parittomat,
        ]
    )

    return muunnos


def _ifft(data):
    """
    iFFT : inverse Fast Fourier Transform : käänteinen Nopea Fourier-Muunnos

    Muuttujat:
    data = Syöte taulukko

    Palauttaa käänteisesti Fourier-muunnetun data taulukon
    """

    pituus = len(data)

    if pituus == 1:
        return data

    parilliset = _ifft(data[::2])
    parittomat = _ifft(data[1::2])

    yksikkojuuret = np.exp(2j * np.pi * np.arange(pituus) / pituus)
    yksikkojuuretJaettu = np.array_split(yksikkojuuret, 2)

    muunnos = np.concatenate(
        [
            (parilliset + yksikkojuuretJaettu[0] * parittomat) / 2,
            (parilliset + yksikkojuuretJaettu[1] * parittomat) / 2,
        ]
    )

    return muunnos


def suorita_fft_datalle(data, omaFFTtoteutus=True):
    if omaFFTtoteutus:
        muunnos = _fft(data)
    else:
        muunnos = fft.fft(data)

    return muunnos


def suorita_ifft_datalle(data, omaiFFTtoteutus=True):
    if omaiFFTtoteutus:
        muunnos = _ifft(data)
    else:
        muunnos = fft.ifft(data)

    return muunnos
