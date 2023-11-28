from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from os import getcwd as cwd

import re

class taajuudenpoisto:
    def __init__(self, ikkuna=Tk):
        self.ruutu = ttk.Frame(ikkuna)
        self.ruutu.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(self.ruutu, text="Valitse tiedosto:").grid(column=1, row=1, sticky=E)
        self.tiedosto = StringVar()
        tiedosto_teksti = ttk.Label(self.ruutu, text="")
        tiedosto_teksti.grid(column=3, row=1, sticky=E)
        tiedosto_syote = ttk.Button(self.ruutu, text="Selaa:", command=lambda: self.valitse_tiedosto(sijainti=self.tiedosto, teksti=tiedosto_teksti))
        tiedosto_syote.grid(column=2, row=1, sticky=(W, E))
        

        ttk.Label(self.ruutu, text="Poistettava taajuus:").grid(column=1, row=2, sticky=E)
        self.taajuus = StringVar()
        taajuus_syote = ttk.Entry(self.ruutu, width=7, textvariable=self.taajuus, validate='key')
        taajuus_syote.grid(column=2, row=2, sticky=(W, E))
        ttk.Label(self.ruutu, text="Hz").grid(column=3, row=2, sticky=W)

        ttk.Label(self.ruutu, text="Voimakkuuden vähennys:").grid(column=1, row=3, sticky=W)
        self.voimakkuus = StringVar()
        voimakkuus_syote = ttk.Entry(self.ruutu, width=7, textvariable=self.voimakkuus, validate='key')
        voimakkuus_syote.grid(column=2, row=3, sticky=(W, E))
        ttk.Label(self.ruutu, text="Db").grid(column=3, row=3, sticky=W)

        ttk.Button(self.ruutu, text="Prosessoi", command=lambda: self.prosessoi()).grid(column=3, row=4, sticky=W)

        for lapsi in self.ruutu.winfo_children(): 
            lapsi.grid_configure(padx=5, pady=5)

        tiedosto_syote.focus()
        ikkuna.bind("<Return>", self.prosessoi)
    
    def vaihda_ruutuun(self):
        self.ruutu.tkraise()
    
    
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

class kuvaajaruutu:
    def __init__(self, ikkuna=Tk):
        self.ruutu = ttk.Frame(ikkuna)
        self.ruutu.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(self.ruutu, text="Valitse tiedosto:").grid(column=1, row=1, sticky=E)
        self.tiedosto = StringVar()
        tiedosto_teksti = ttk.Label(self.ruutu, text="")
        tiedosto_teksti.grid(column=3, row=1, sticky=E)
        tiedosto_syote = ttk.Button(self.ruutu, text="Selaa:", command=lambda: self.valitse_tiedosto(sijainti=self.tiedosto, teksti=tiedosto_teksti))
        tiedosto_syote.grid(column=2, row=1, sticky=(W, E))
        

        ttk.Label(self.ruutu, text="Suoritetaan fft").grid(column=1, row=2, sticky=E)
        self.suoritetaanko_fft = IntVar(value=0)
        suoritetaanko_fft_syote = ttk.Checkbutton(
            self.ruutu, width=7, variable=self.suoritetaanko_fft)
        suoritetaanko_fft_syote.grid(column=2, row=2, sticky=(W, E))

        ttk.Label(self.ruutu, text="Suoritetaan ifft").grid(column=1, row=3, sticky=W)
        self.suoritetaanko_ifft = IntVar(value=0)
        suoritetaanko_ifft_syote = ttk.Checkbutton(
            self.ruutu, width=7, variable=self.suoritetaanko_ifft)
        suoritetaanko_ifft_syote.grid(column=2, row=3, sticky=(W, E))

        ttk.Button(self.ruutu, text="Prosessoi", command=lambda: self.prosessoi()).grid(column=3, row=4, sticky=W)

        for lapsi in self.ruutu.winfo_children(): 
            lapsi.grid_configure(padx=5, pady=5)

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
        print("Sijainti: ", self.tiedosto.get(), ", Suoritetaanko fft: ", self.suoritetaanko_fft.get(), "Suoritetaanko ifft: ", self.suoritetaanko_ifft.get())

    
    def vaihda_ruutuun(self):
        self.ruutu.tkraise()

class aloitusruutu:

    def __init__(self, ikkuna=Tk):
        self.ruutu = ttk.Frame(ikkuna)
        self.ruutu.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(self.ruutu, text="Kohinanpoistotyökalu").grid(column=1, row=1, sticky=E)
        ttk.Label(self.ruutu, text="Tähän tulee tekstiä.").grid(column=1, row=2, sticky=E)
    
    def vaihda_ruutuun(self):
        self.ruutu.tkraise()

class valikko:

    def __init__(self, rajapinta, ikkuna=Tk):
        self.rajapinta = rajapinta
        self.valikko = Menu(ikkuna)
        ikkuna['menu']=self.valikko

        self.visualisointi_valikko = Menu(self.valikko)
        self.suodatus_valikko = Menu(self.valikko)

        self.valikko.add_command(
            label='aloitus', 
            command = lambda : self.rajapinta.vaihda_ruutua('aloitus'))

        self.valikko.add_cascade(menu=self.suodatus_valikko, label='suodatus')
        self.suodatus_valikko.add_command(
            label='voimakkain taajuus', 
            command = lambda : self.rajapinta.vaihda_ruutua('voimakkain taajuus'))
        self.suodatus_valikko.add_command(
            label='valitse taajuus', 
            command = lambda : self.rajapinta.vaihda_ruutua('valitse taajuus'))

        self.valikko.add_cascade(menu=self.visualisointi_valikko, label='visualisoi')
        self.visualisointi_valikko.add_command(
            label='kuvaaja', 
            command = lambda : self.rajapinta.vaihda_ruutua('kuvaaja'))
        self.visualisointi_valikko.add_command(
            label='vertaile toteutuksia', 
            command = lambda : self.rajapinta.vaihda_ruutua('vertaile toteutuksia'))




class kayttoliittyma:
    '''
    Käyttöliittymä

    Toteuttaa kohinanpoistosovellukselle käyttöliittymän, jolla sitä käytetään.
    '''
    def __init__(self, ikkuna):
        ikkuna.title("Kohinanpoistotyökalu")
        self.taajuuden_poisto = taajuudenpoisto(ikkuna)
        self.kuvaaja_ruutu = kuvaajaruutu(ikkuna)
        self.aloitus_ruutu = aloitusruutu(ikkuna)
        self.valikko = valikko(self, ikkuna)

    def vaihda_ruutua(self, vaihdettavan_nimi):
        if vaihdettavan_nimi == 'aloitus':
            self.aloitus_ruutu.vaihda_ruutuun()
        elif vaihdettavan_nimi == 'valitse taajuus':
            self.taajuuden_poisto.vaihda_ruutuun()
        elif vaihdettavan_nimi == 'voimakkain taajuus':
            1
        elif vaihdettavan_nimi == 'kuvaaja':
            self.kuvaaja_ruutu.vaihda_ruutuun()
        elif vaihdettavan_nimi == 'vertaile toteutuksia':
            1
        else:
            self.aloitus_ruutu.vaihda_ruutuun()
    

if __name__ == "__main__":
    ikkuna = Tk()
    ikkuna.option_add("*tearOff", False)
    kayttoliittyma(ikkuna)
    ikkuna.mainloop()
