import matplotlib.pyplot as plt
import scipy.fftpack as fft
from scipy.io import wavfile
import numpy as np

import math


def FFT(data):
    '''
    FFT : Fast Fourier Transform : Nopea Fourier-Muunnos

    Muuttujat:
    data = Syöte taulukko
    
    Palauttaa Fourier-muunnetun data taulukon  
    '''

    pituus = len(data)
    

    if pituus == 1:
        return data
    else:

        #Rekursio
        parilliset = FFT(data[::2])
        parittomat = FFT(data[1::2])

        yksikkojuuret = np.exp(-2j*np.pi*np.arange(pituus)/ pituus)
        yksikkojuuretJaettu=np.array_split(yksikkojuuret, 2)

        try:
            muunnos = np.concatenate([parilliset+yksikkojuuretJaettu[0]*parittomat, parilliset+yksikkojuuretJaettu[1]*parittomat])
        except ValueError as e:
            print(len(yksikkojuuretJaettu[0]), ":", len(parittomat), ":", len(parilliset), ";", pituus)
            print(data)
            raise
        return muunnos
    

def iFFT(data):
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

        #Rekursio
        parilliset = FFT(data[::2])
        parittomat = FFT(data[1::2])

        yksikkojuuret = np.exp(2j*np.pi*np.arange(pituus)/ pituus)
        yksikkojuuretJaettu=np.array_split(yksikkojuuret, 2)

        try:
            muunnos = np.concatenate([parilliset+yksikkojuuretJaettu[0]*parittomat, parilliset+yksikkojuuretJaettu[1]*parittomat])
        except ValueError as e:
            print(len(yksikkojuuretJaettu[0]), ":", len(parittomat), ":", len(parilliset), ";", pituus)
            print(data)
            raise
        return muunnos


def scipy_fft(data):
    return fft.fft(data)

def scipy_ifft(data):
    return fft.ifft(data)






if __name__ == "__main__":
    #
    # Tämä on vasta testausversio ja ei sen vuoksi ole kirjoitettu mitenkään järkevästi kutsuttavaksi.
    # Piti ensin saada fft toimimaan ja yrittää ymmärtää sitä hieman paremmin.


    # Datan lukeminen
    fs, data = wavfile.read('./Syotteet/Club_BigBassHits_136_Gm.wav')
    #fs, data = wavfile.read('./Syotteet/atmosphere_forest_birds.wav')

    # Tiedostossa on kaksi ääniraitaa, niin valitsin ensimmäisen
    data = data.T[0] 

    # Tarkistetaan, että data on muotoa pituus=n^2. Jos ei ole, lisätään dataan n^2-pituus nollaa.
    pituus = len(data)
    log2pituus = np.log2(pituus)
    if not log2pituus.is_integer():
        pituusNormalisoitu = math.pow(2,math.ceil(log2pituus))
        data = np.append(data, [0 for i in range(int(pituusNormalisoitu-pituus))])

        if len(data) != pituusNormalisoitu:
            print(pituus, len(data), pituusNormalisoitu)
            raise

    #Tässä on oma algoritmini FFT ja scipy kirjaston huomattavasti nopeampi algoritmi fft, jota voi vertailla
    muunnos = FFT(data) #Oma
    #muunnos = fft(data) #scipy

    #muunnos = iFFT(muunnos)

    # Piirretään kuvaaja (piirretään vain puolet, koska kuvaaja on symmetrinen)
    kuvaajanPituus = int(len(muunnos))
    #plt.plot(abs(muunnos[:(kuvaajanPituus-1)]),'r') 

    otsikko, (kuvaaja1, kuvaaja2, kuvaaja3) = plt.subplots(3)
    otsikko.suptitle('FFT vertailu')
    kuvaaja1.plot(abs(muunnos[:(kuvaajanPituus-1)]),'r')


    muunnos = fft.fft(data) #scipy

    #muunnos = fft.ifft(muunnos)
    kuvaajanPituus = int(len(muunnos))
    kuvaaja2.plot(abs(muunnos[:(kuvaajanPituus-1)]),'r')

    kuvaaja3.plot(data, 'r')


    plt.show()



