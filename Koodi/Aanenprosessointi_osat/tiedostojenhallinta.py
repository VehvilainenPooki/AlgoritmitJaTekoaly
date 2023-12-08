from scipy.io import wavfile

import numpy as np
import math


def _kasvata_data_sopivan_pituiseksi(data):
    """
    Tarkistaa, että <data> on muotoa pituus=2^n. Jos ei ole, lisätään dataan 2^n-pituus nollaa.

    Palauttaa nollilla kasvatetun taulukon muotoa 2^n.
    """
    pituus = len(data)
    log2pituus = np.log2(pituus)
    if not log2pituus.is_integer():
        pituusNormalisoitu = math.pow(2, math.ceil(log2pituus))
        data = np.append(data, [0 for i in range(int(pituusNormalisoitu - pituus))])

    return data


def lue_wav_tiedosto(polku):
    """
    Lukee <polku> osoitteessa olevan .wav tiedoston ja prosessoi sen fft algoritmilleni sopivaksi.

    Palauttaa
    <naytteenottoTaajuus> .wav tiedoston näytteenottotaajuus
    <data> .wav tiedoston data tauluna,
        johon on lisätty perään nollia niin, että taulun pituus on muotoa 2**n.
        Nollien lisäys on fft algoritmia varten.
    """
    naytteenottoTaajuus, data = wavfile.read(polku)

    data = data.T[0]

    data = _kasvata_data_sopivan_pituiseksi(data)

    return naytteenottoTaajuus, data


def tallenna_tiedosto(polku, data, otostiheys):
    if polku[len(polku) - 4 :] != ".wav":
        polku = polku + ".wav"
    wavfile.write(polku, otostiheys, data.astype(np.int16))
