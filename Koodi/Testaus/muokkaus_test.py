import unittest
import numpy as np
import random

from Koodi.Aanenprosessointi_osat import muokkaus
from Koodi.Aanenprosessointi_osat import tiedostojenhallinta



class TestAlgoritmi(unittest.TestCase):
    
    def test_voimakkain(self):
        """
        Randomisoitu testaus voimakkain_signaali funktiolle.
        100 kertaa 100 satunnaista lukua väliltä 0-100.
        """
        for toistot in range(100):
            isoin = -1
            isoinIndeksi = -1
            testiTaulu = []
            for i in range(50):
                luku = random.randint(0, 100)
                if isoin < luku:
                    isoin = luku
                    isoinIndeksi = i
                testiTaulu.append(luku)

            #FFT data on symmetrinen, joten vain puolet taulusta on relevanttia.
            for i in range(50):
                testiTaulu.append(0)
            
            kohta = muokkaus.voimakkain_signaali(testiTaulu)
            
            if kohta != isoinIndeksi:
                assert kohta == isoinIndeksi, "Voimakkaimman signaalin tunnistaminen ei toimi oikein."
        
        assert True



    def test_kohdan_poisto(self):
        """
        Randomisoitu testaus poista_signaali funktiolle.
        100 kertaa 100 satunnaista lukua väliltä 0-100.
        """
        for toistot in range(100):
            for toistot in range(100):
                testiTaulu = []
                for i in range(100):
                    luku = random.randint(1, 99)
                    testiTaulu.append(luku)
            
            poistokohta = random.randint(0, 49)
            poistoleveys = random.randint(1, 100)
            testiTaulu = muokkaus.poista_signaali(testiTaulu, poistokohta, poistoleveys)

            for i in range(poistoleveys * 2 + 1):
                kohta = poistokohta + i - poistoleveys
                if 99 / 2 > kohta > -1:
                    if testiTaulu[kohta] != 0 + 0j or testiTaulu[99 - kohta] != 0 + 0j:
                        assert testiTaulu[kohta] == 0 + 0j and testiTaulu[100 - kohta] == 0 + 0j, "Kohdan poisto ei toimi oikein."

        assert True