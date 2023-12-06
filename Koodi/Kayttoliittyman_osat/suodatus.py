from os import getcwd as cwd

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

import aanenprosessointi



class taajuudenpoisto:
    def __init__(self, ikkuna=Tk):
        self.ruutu = ttk.Frame(ikkuna)
        self.ruutu.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(self.ruutu, text="Valitse tiedosto:").grid(column=1, row=1, sticky=E)
        self.tiedosto = StringVar()
        tiedosto_teksti = ttk.Label(self.ruutu, text="")
        tiedosto_teksti.grid(column=3, row=1, sticky=E)

        tiedosto_syote = ttk.Button(
            self.ruutu,
            text="Selaa:",
            command=lambda: self.valitse_tiedosto(sijainti=self.tiedosto, teksti=tiedosto_teksti))
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

