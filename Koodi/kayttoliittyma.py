from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from os import getcwd as cwd

import re


class kayttoliittyma:
    '''
    Käyttöliittymä

    Toteuttaa kohinanpoistosovellukselle käyttöliittymän, jolla sitä käytetään.
    '''
    def __init__(self, ikkuna):
        ikkuna.title("Kohinanpoistotyökalu")
        self._luo_aloitus_ruutu(ikkuna)
        self._luo_taajuuden_poisto(ikkuna)

    def _luo_aloitus_ruutu(self, ikkuna):
        1#Työn alla

    def _luo_taajuuden_poisto(self, ikkuna):
        ruutu = ttk.Frame(ikkuna)
        ruutu.grid(column=0, row=0, sticky=(N, W, E, S))

        check_num_wrapper = (ikkuna.register(self.check_num), '%P')

        ttk.Label(ruutu, text="Valitse tiedosto:").grid(column=1, row=1, sticky=E)
        self.tiedosto = StringVar()
        tiedosto_teksti = ttk.Label(ruutu, text="")
        tiedosto_teksti.grid(column=3, row=1, sticky=E)
        tiedosto_syote = ttk.Button(ruutu, text="Selaa:", command=lambda: self.valitse_tiedosto(sijainti=self.tiedosto, teksti=tiedosto_teksti))
        tiedosto_syote.grid(column=2, row=1, sticky=(W, E))
        

        ttk.Label(ruutu, text="Poistettava taajuus:").grid(column=1, row=2, sticky=E)
        self.taajuus = StringVar()
        taajuus_syote = ttk.Entry(ruutu, width=7, textvariable=self.taajuus, validate='key', validatecommand=check_num_wrapper)
        taajuus_syote.grid(column=2, row=2, sticky=(W, E))
        ttk.Label(ruutu, text="Hz").grid(column=3, row=2, sticky=W)

        ttk.Label(ruutu, text="Voimakkuuden vähennys:").grid(column=1, row=3, sticky=W)
        self.voimakkuus = StringVar()
        voimakkuus_syote = ttk.Entry(ruutu, width=7, textvariable=self.voimakkuus, validate='key', validatecommand=check_num_wrapper)
        voimakkuus_syote.grid(column=2, row=3, sticky=(W, E))
        ttk.Label(ruutu, text="Db").grid(column=3, row=3, sticky=W)

        ttk.Button(ruutu, text="Prosessoi", command=lambda: self.prosessoi()).grid(column=3, row=4, sticky=W)

        for lapsi in ruutu.winfo_children(): 
            lapsi.grid_configure(padx=5, pady=5)

        tiedosto_syote.focus()
        ikkuna.bind("<Return>", self.prosessoi)

    def check_num(self, newval):
        return re.match('^[0-9]*$', newval) is not None and len(newval) <= 6

    def prosessoi(self):
        #Työn alla
        print("Sijainti: ", self.tiedosto.get(), ", Taajuus: ", self.taajuus.get(), "Hz, Voimakkuus: ", self.voimakkuus.get(), "Db")

    def valitse_tiedosto(self, sijainti, teksti):
        dir = cwd() + "/Syotteet/"
        tiedosto = filedialog.askopenfilename(initialdir=dir, filetypes=[('Audio',['*.wav', '*.mp3'])])
        sijainti.set(tiedosto)
        i = tiedosto.rfind("/")
        if i != -1:
            tiedosto = tiedosto[i+1: ]

        teksti.config(text=tiedosto)

ikkuna = Tk()
kayttoliittyma(ikkuna)
ikkuna.mainloop()
