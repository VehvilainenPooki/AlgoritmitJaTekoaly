from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from os import getcwd as cwd

import re

class taajuudenpoisto:
    def __init__(self, ikkuna=Tk):
        ruutu = ttk.Frame(ikkuna)
        ruutu.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(ruutu, text="Valitse tiedosto:").grid(column=1, row=1, sticky=E)
        self.tiedosto = StringVar()
        tiedosto_teksti = ttk.Label(ruutu, text="")
        tiedosto_teksti.grid(column=3, row=1, sticky=E)
        tiedosto_syote = ttk.Button(ruutu, text="Selaa:", command=lambda: self.valitse_tiedosto(sijainti=self.tiedosto, teksti=tiedosto_teksti))
        tiedosto_syote.grid(column=2, row=1, sticky=(W, E))
        

        ttk.Label(ruutu, text="Poistettava taajuus:").grid(column=1, row=2, sticky=E)
        self.taajuus = StringVar()
        taajuus_syote = ttk.Entry(ruutu, width=7, textvariable=self.taajuus, validate='key')
        taajuus_syote.grid(column=2, row=2, sticky=(W, E))
        ttk.Label(ruutu, text="Hz").grid(column=3, row=2, sticky=W)

        ttk.Label(ruutu, text="Voimakkuuden vähennys:").grid(column=1, row=3, sticky=W)
        self.voimakkuus = StringVar()
        voimakkuus_syote = ttk.Entry(ruutu, width=7, textvariable=self.voimakkuus, validate='key')
        voimakkuus_syote.grid(column=2, row=3, sticky=(W, E))
        ttk.Label(ruutu, text="Db").grid(column=3, row=3, sticky=W)

        ttk.Button(ruutu, text="Prosessoi", command=lambda: self.prosessoi()).grid(column=3, row=4, sticky=W)

        for lapsi in ruutu.winfo_children(): 
            lapsi.grid_configure(padx=5, pady=5)

        tiedosto_syote.focus()
        ikkuna.bind("<Return>", self.prosessoi)
    
    
    def valitse_tiedosto(self, sijainti, teksti):
        dir = cwd() + "/Syotteet/"
        tiedosto = filedialog.askopenfilename(initialdir=dir, filetypes=[('Audio',['*.wav', '*.mp3'])])
        sijainti.set(tiedosto)
        i = tiedosto.rfind("/")
        if i != -1:
            tiedosto = tiedosto[i+1: ]

        teksti.config(text=tiedosto)

    def prosessoi(self):
        #Työn alla
        print("Sijainti: ", self.tiedosto.get(), ", Taajuus: ", self.taajuus.get(), "Hz, Voimakkuus: ", self.voimakkuus.get(), "Db")


class aloitusruutu:

    def __init__(self, ikkuna):
        1


class valikko:

    def __init__(self, ikkuna=Tk):
        valikko = Menu(ikkuna)
        ikkuna['menu']=valikko

        visualisointi_valikko = Menu(valikko)
        suodatus_valikko = Menu(valikko)

        valikko.add_command(label='aloitus')

        valikko.add_cascade(menu=suodatus_valikko, label='suodatus')
        suodatus_valikko.add_command(label='voimakkain taajuus')
        suodatus_valikko.add_command(label='valitse taajuus')

        valikko.add_cascade(menu=visualisointi_valikko, label='visualisoi')
        visualisointi_valikko.add_command(label='kuvaaja')
        visualisointi_valikko.add_command(label='vertaile toteutuksia')




class kayttoliittyma:
    '''
    Käyttöliittymä

    Toteuttaa kohinanpoistosovellukselle käyttöliittymän, jolla sitä käytetään.
    '''
    def __init__(self, ikkuna):
        ikkuna.title("Kohinanpoistotyökalu")
        self.aloitus_ruutu = aloitusruutu(ikkuna)
        self.valikko = valikko(ikkuna)
        self.taajuuden_poisto = taajuudenpoisto(ikkuna)

    

if __name__ == "__main__":
    ikkuna = Tk()
    ikkuna.option_add("*tearOff", False)
    kayttoliittyma(ikkuna)
    ikkuna.mainloop()
