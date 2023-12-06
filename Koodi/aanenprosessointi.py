import matplotlib.pyplot as plt

from scipy.io import wavfile
import numpy as np

from Aanenprosessointi_osat import algoritmi, muokkaus, tiedostonlukeminen



def FFT_tiedostolle(tiedostonOsoite, omaFFTtoteutus=True):
    '''
    Lasketaan FFT annetusta tiedostosta.

    muuttujat:
    tiedostonOsoite = täysi tai relatiivinen osoite tiedostolle
    omaFFTtoteutus = Käytetäänkö omaa vai Scipy kirjaston FFT toteutusta # Default : True

    Palauttaa FFT muunnetun taulukon. Taulukko on kaksiulotteinen. Muotoa [[dataOtokset], [kanavat]]
    '''
    naytteenottoTaajuus, data = tiedostonlukeminen.lue_wav_tiedosto(tiedostonOsoite)

    return algoritmi.suorita_FFT_datalle(data, omaFFTtoteutus)


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



