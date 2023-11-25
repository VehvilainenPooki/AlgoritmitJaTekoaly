import matplotlib.pyplot as plt
import scipy.fftpack as fft
from scipy.io import wavfile
import numpy as np

import math


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

def _suorita_FFT_datalle(data, omaFFTtoteutus=True):
    if omaFFTtoteutus:
        muunnos = _FFT(data)
    else:
        muunnos = fft.fft(data)

    return muunnos

def _suorita_iFFT_datalle(data, omaFFTtoteutus):
    if omaFFTtoteutus:
        muunnos = _FFT(data)
    else:
        muunnos = fft.fft(data)

    return muunnos

def FFT_tiedostolle(tiedostonOsoite, omaFFTtoteutus=True):
    '''
    Lasketaan FFT annetusta tiedostosta.

    muuttujat:
    tiedostonOsoite = täysi tai relatiivinen osoite tiedostolle
    omaFFTtoteutus = Käytetäänkö omaa vai Scipy kirjaston FFT toteutusta # Default : True

    Palauttaa FFT muunnetun taulukon. Taulukko on kaksiulotteinen. Muotoa [[dataOtokset], [kanavat]]
    '''
    naytteenottoTaajuus, data = wavfile.read(tiedostonOsoite)

    data = data.T[0]

    return _suorita_FFT_datalle(_kasvata_data_sopivan_pituiseksi(data))



if __name__ == "__main__":
    '''
    FFT:n testausta ilman muun projektin osia.
    '''

    #Testitiedostoja
    tiedosto = './Syotteet/Club_BigBassHits_136_Gm.wav'
    #tiedosto = './Syotteet/atmosphere_forest_birds.wav'

    otsikko, (kuvaaja1, kuvaaja2, kuvaaja3) = plt.subplots(3)
    otsikko.suptitle('FFT vertailu')
    kuvaaja1.plot(FFT_tiedostolle(tiedosto, True),'r')

    kuvaaja2.plot(FFT_tiedostolle(tiedosto, False),'r')

    turha, data = wavfile.read(tiedosto)
    kuvaaja3.plot(data.T[0], 'r')

    plt.show()



