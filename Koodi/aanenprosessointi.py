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

def poista_voimakkain_signaali(fftData=np.array, poistoLeveys=int):
    '''
    Poistaa FFT prosessoidusta yksi-ulotteisesta datasta voimakkaimman signaalin.

    Muuttujat:
    fftData = fft:llä prosessoitu äänidata
    poistoLeveys = Kuinka monta otosta poistetaan voimakkaimman signaalin kummaltakin puolelta

    : Palauttaa prosessoidun datan
    '''
    data = fftdata.copy()
    voimakkainKohta = _voimakkain_signaali(data)
    return _poista_signaali(data, voimakkainKohta, poistoLeveys)

def _voimakkain_signaali(fftData=np.array):
    '''
    Etsii fft datasta voimakkaaimman data pisteen ja palauttaa sen indexin
    '''
    voimakkain = 0
    voimakkainKohta = -1
    datanPituus = int(len(fftData)/2)
    for kohta in range(datanPituus):
        arvo = fftData[kohta]
        if voimakkain < abs(arvo):
            voimakkain = abs(arvo)
            voimakkainKohta = kohta
    return voimakkainKohta
    
def _poista_signaali(fftData=np.array, poistoKohta=int, poistoLeveys=int):
    '''
    Asettaa <poistoKohta> muuttujan kohdan ympäriltä <poistoLeveys> muuttujan kokoisen välin nollaksi

    Muuttujat:
    fftData = fft prosessoitu äänidata
    poistoKohta = Kohta, jonka ympäriltä nollataan data
    poistoLeveys = Leveys, joka nollataan poistoKohdan ympäriltä.

    Palauttaa muunnetun fftData taulukon
    '''
    datanPituus = len(fftData)
    for i in range(poistoLeveys*2+1):
        kohta = poistoKohta+i-poistoLeveys
        if datanPituus/2 > kohta and -1 < kohta:
            fftData[kohta]=0+0j
            fftData[datanPituus-kohta]=0+0J
            
    return fftData


if __name__ == "__main__":
    '''
    FFT:n testausta ilman muun projektin osia.
    '''

    #Testitiedostoja
    #tiedosto = './Syotteet/Testi1IlmanSini.wav'
    #tiedosto = './Syotteet/Testi1SiniAallolla.wav'
    #tiedosto = './Syotteet/Testi2Siniaaltoja.wav'
    tiedosto = './Syotteet/Testi3Siniaaltoja2.wav'



    otsikko, (kuvaaja1, kuvaaja2, kuvaaja3) = plt.subplots(3)
    otsikko.suptitle('FFT vertailu')


    #Generoidaan FFT data: True = käytetään omaa fft, False = käytetään scipy.fft (nopeampi)
    fftdata = FFT_tiedostolle(tiedosto, False)

    #Piirretään signaalinpoistoalue
    voimakkainKohta = _voimakkain_signaali(fftdata)
    poistonLeveys = 100
    kuvaaja1.axvline(x=voimakkainKohta+poistonLeveys, color='b')
    kuvaaja1.axvline(x=voimakkainKohta-poistonLeveys, color='b')
    # Piirretään fftdata. Voit rajata valintaa lisäämällä plot kohtaan fftdata[:lopetuspiste]
    kuvaaja1.plot(fftdata[:],'r')




    #Piirretään fftdata, josta on poistettu voimakkain signaali.
    # Voit rajata valintaa lisäämällä plot kohtaan voimakkainPoistettu[:lopetuspiste]
    voimakkainPoistettu = poista_voimakkain_signaali(fftdata, poistonLeveys)
    kuvaaja2.plot(voimakkainPoistettu[:],'r')

    #Piirretään kuvaaja äänitiedostosta
    otostiheys, data = wavfile.read(tiedosto)
    kuvaaja3.plot(data.T[0], 'r')

    #Luo wav Tiedoston, josta on poistettu voimakkain signaali.
    #Huomaa, että tällä hetkellä FFT on vain yksikanavainen,
    #joten luodun tiedoston laatu ei ole ihan yhtä hyvä.
    #Toiminnan huomaa parhaiten Testi1SiniAallolla.wav ja vertaa tulosta Testi1IlmanSini.wav
    wavfile.write(filename="testi.wav",data=fft.ifft(x=voimakkainPoistettu).astype(np.int16), rate=otostiheys)
    
    plt.show()



