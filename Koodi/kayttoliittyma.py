from tkinter import *

from os import getcwd as cwd

from Kayttoliittyman_osat import aloitus, visualisointi, suodatus


class valikko:
    def __init__(self, rajapinta, ikkuna=Tk):
        self.rajapinta = rajapinta
        self.valikko = Menu(ikkuna)
        ikkuna["menu"] = self.valikko

        self.visualisointi_valikko = Menu(self.valikko)
        self.suodatus_valikko = Menu(self.valikko)

        self.valikko.add_command(
            label="aloitus", command=lambda: self.rajapinta.vaihda_ruutua("aloitus")
        )

        self.valikko.add_cascade(menu=self.suodatus_valikko, label="suodatus")
        self.suodatus_valikko.add_command(
            label="voimakkain taajuus",
            command=lambda: self.rajapinta.vaihda_ruutua("voimakkain taajuus"),
        )
        self.suodatus_valikko.add_command(
            label="valitse taajuus",
            command=lambda: self.rajapinta.vaihda_ruutua("valitse taajuus"),
        )

        self.valikko.add_cascade(menu=self.visualisointi_valikko, label="visualisointi")
        self.visualisointi_valikko.add_command(
            label="kuvaaja", command=lambda: self.rajapinta.vaihda_ruutua("kuvaaja")
        )
        self.visualisointi_valikko.add_command(
            label="vertaile", command=lambda: self.rajapinta.vaihda_ruutua("vertaile")
        )


class kayttoliittyma:
    """
    Käyttöliittymä

    Toteuttaa kohinanpoistosovellukselle käyttöliittymän, jolla sitä käytetään.
    """

    def __init__(self, ikkuna):
        ikkuna.title("Kohinanpoistotyökalu")
        self.taajuuden_poisto = suodatus.taajuudenpoisto(ikkuna)
        self.voimakkaimman_poisto = suodatus.voimakkaimmanpoisto(ikkuna)
        self.kuvaaja_ruutu = visualisointi.kuvaajaruutu(ikkuna)
        self.vertailu_ruutu = visualisointi.vertailuruutu(ikkuna)
        self.aloitus_ruutu = aloitus.aloitusruutu(ikkuna)
        self.valikko = valikko(self, ikkuna)

    def vaihda_ruutua(self, vaihdettavan_nimi):
        if vaihdettavan_nimi == "aloitus":
            self.aloitus_ruutu.vaihda_ruutuun()
        elif vaihdettavan_nimi == "valitse taajuus":
            self.taajuuden_poisto.vaihda_ruutuun()
        elif vaihdettavan_nimi == "voimakkain taajuus":
            self.voimakkaimman_poisto.vaihda_ruutuun()
        elif vaihdettavan_nimi == "kuvaaja":
            self.kuvaaja_ruutu.vaihda_ruutuun()
        elif vaihdettavan_nimi == "vertaile":
            self.vertailu_ruutu.vaihda_ruutuun()
        else:
            self.aloitus_ruutu.vaihda_ruutuun()


if __name__ == "__main__":
    ikkuna = Tk()
    ikkuna.option_add("*tearOff", False)
    kayttoliittyma(ikkuna)
    ikkuna.mainloop()
