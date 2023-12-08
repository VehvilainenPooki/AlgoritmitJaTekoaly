"""
Käyttöliittymä

Moduuli on Sovelluksen päämoduuli. Se integroi käyttöliittymän välilehdet.
"""
from tkinter import (Tk,Menu)

from Kayttoliittyman_osat import aloitus, visualisointi, suodatus

class Valikko:
    """
    Valikko

    Luokka luo yläreunan valikon käyttöliittymälle.
    """
    def __init__(self, rajapinta, ikkuna=Tk):
        self.rajapinta = rajapinta
        self.valikko = Menu(ikkuna)
        ikkuna["menu"] = self.valikko

        self.visualisointiValikko = Menu(self.valikko)
        self.suodatusValikko = Menu(self.valikko)

        self.valikko.add_command(
            label="aloitus", command=lambda: self.rajapinta.vaihda_ruutua("aloitus")
        )

        self.valikko.add_cascade(menu=self.suodatusValikko, label="suodatus")
        self.suodatusValikko.add_command(
            label="voimakkain taajuus",
            command=lambda: self.rajapinta.vaihda_ruutua("voimakkain taajuus"),
        )
        self.suodatusValikko.add_command(
            label="valitse taajuus",
            command=lambda: self.rajapinta.vaihda_ruutua("valitse taajuus"),
        )

        self.valikko.add_cascade(menu=self.visualisointiValikko, label="visualisointi")
        self.visualisointiValikko.add_command(
            label="kuvaaja", command=lambda: self.rajapinta.vaihda_ruutua("kuvaaja")
        )
        self.visualisointiValikko.add_command(
            label="vertaile", command=lambda: self.rajapinta.vaihda_ruutua("vertaile")
        )


class Kayttoliittyma:
    """
    Käyttöliittymä

    Toteuttaa kohinanpoistosovellukselle käyttöliittymän, jolla sitä käytetään.
    """

    def __init__(self):
        ikkuna = Tk()
        ikkuna.option_add("*tearOff", False)
        ikkuna.title("Kohinanpoistotyökalu")
        self.taajuudenpoisto = suodatus.Taajuudenpoisto(ikkuna)
        self.voimakkaimmanpoisto = suodatus.Voimakkaimmanpoisto(ikkuna)
        self.kuvaajaruutu = visualisointi.Kuvaajaruutu(ikkuna)
        self.vertailuruutu = visualisointi.Vertailuruutu(ikkuna)
        self.aloitusruutu = aloitus.Aloitusruutu(ikkuna)
        self.valikko = Valikko(self, ikkuna)
        ikkuna.mainloop()

    def vaihda_ruutua(self, vaihdettavanNimi):
        if vaihdettavanNimi == "aloitus":
            self.aloitusruutu.vaihda_ruutuun()
        elif vaihdettavanNimi == "valitse taajuus":
            self.taajuudenpoisto.vaihda_ruutuun()
        elif vaihdettavanNimi == "voimakkain taajuus":
            self.voimakkaimmanpoisto.vaihda_ruutuun()
        elif vaihdettavanNimi == "kuvaaja":
            self.kuvaajaruutu.vaihda_ruutuun()
        elif vaihdettavanNimi == "vertaile":
            self.vertailuruutu.vaihda_ruutuun()
        else:
            self.aloitusruutu.vaihda_ruutuun()


if __name__ == "__main__":
    Kayttoliittyma()
