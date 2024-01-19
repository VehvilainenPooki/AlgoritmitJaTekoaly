import unittest
import numpy as np
import random
import math

from Koodi.Aanenprosessointi_osat import algoritmi
from Koodi.Aanenprosessointi_osat import tiedostojenhallinta


data = tiedostojenhallinta.lue_wav_tiedosto("C:/Users/Potsu/Desktop/Uni/Algoritmit ja tekoäly/AlgoritmitJaTekoaly/Koodi/Syotteet/Testi3Siniaaltoja2.wav")[1]

class TestAlgoritmi(unittest.TestCase):
    
    def test_datan_kasvatus(self):
        """
        Randomisoitu testaus datan kasvatukselle.
        100 kertaa 10-100000 pituisen taulun kasvatus.
        """
        for i in range(100):
            alkupituus = random.randint(10,100000)
            data = [1]*alkupituus
            data = tiedostojenhallinta._kasvata_data_sopivan_pituiseksi(data)
            if len(data) != math.pow(2, math.ceil(np.log2(alkupituus))):
                assert len(data) == math.pow(2, math.ceil(np.log2(alkupituus))), "Datan kasvatus ei toimi oikein."
        assert True
    
    def test_FFT(self):
        """
        FFT testaus verraten Scipy.IO toteutukseen.
        Testi käyttää Testi3Siniaaltoja2.wav.
        """
        oma = algoritmi.suorita_fft_datalle(data, True)
        scipy = algoritmi.suorita_fft_datalle(data, False)

        print(scipy)

        for i in range(len(oma)):
            erotus = abs(oma[i])-abs(scipy[i])
            if abs(erotus) > 0.01:
                assert abs(erotus) < 0.00001, "fft ei toiminut oikein"

        assert True

    def test_IFFT(self):
        """
        IFFT testaus verraten Scipy.IO toteutukseen.
        Testi käyttää Testi3Siniaaltoja2.wav.
        """
        oma = algoritmi.suorita_ifft_datalle(data, True)
        scipy = algoritmi.suorita_ifft_datalle(data, False)

        for i in range(len(oma)):
            erotus = abs(oma[i])-abs(scipy[i])
            if abs(erotus) > 0.01:
                assert abs(erotus) < 0.00001, "ifft ei toiminut oikein"

        assert True

    def test_FFT_IFFT(self):
        """
        FFT ja IFFT yhteinen testaus verraten alkuperäiseen dataan.
        Testi käyttää Testi3Siniaaltoja2.wav.
        """
        fft = algoritmi.suorita_fft_datalle(data, True)
        fftifft = algoritmi.suorita_ifft_datalle(fft, True)

        for i in range(len(data)):
            erotus = abs(data[i])-abs(fftifft[i])
            if abs(erotus) > 0.01:
                assert abs(erotus) < 0.00001, "fft tai ifft ei toiminut oikein"

        assert True
