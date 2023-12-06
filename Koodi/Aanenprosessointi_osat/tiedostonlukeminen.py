from scipy.io import wavfile

import numpy as np
import math




def _kasvata_data_sopivan_pituiseksi(data):
    '''
    Tarkistaa, että data on muotoa pituus=2^n. Jos ei ole, lisätään dataan 2^n-pituus nollaa.
    '''
    pituus = len(data)
    log2pituus = np.log2(pituus)
    if not log2pituus.is_integer():
        pituusNormalisoitu = math.pow(2,math.ceil(log2pituus))
        data = np.append(data, [0 for i in range(int(pituusNormalisoitu-pituus))])
    
    return data

def lue_wav_tiedosto(polku):
    naytteenottoTaajuus, data = wavfile.read(polku)

    data = data.T[0]

    data = _kasvata_data_sopivan_pituiseksi(data)

    return naytteenottoTaajuus, data

