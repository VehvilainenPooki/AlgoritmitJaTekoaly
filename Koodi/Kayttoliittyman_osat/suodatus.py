from os import getcwd as cwd

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import re

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

from Aanenprosessointi_osat import algoritmi, tiedostojenhallinta, muokkaus



class taajuudenpoisto:
    def __init__(self, ikkuna=Tk):
        self.nykyinenData = None

        self.ruutu = ttk.Frame(ikkuna)
        self.ruutu.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(self.ruutu, text="Valitse tiedosto:").grid(column=1, row=1, sticky=E)
        self.tiedosto = StringVar()
        tiedosto_teksti = ttk.Label(self.ruutu, text="")
        tiedosto_teksti.grid(column=3, row=1, sticky=E)

        tiedosto_syote = ttk.Button(
            self.ruutu,
            text="Selaa:",
            command=lambda: self._valitse_tiedosto(sijainti=self.tiedosto, teksti=tiedosto_teksti))
        tiedosto_syote.grid(column=2, row=1, sticky=(W, E))
        
        self.algoritmiToteutus = IntVar(value=1)
        ttk.Label(self.ruutu, text="Valitse algoritmin toteutus:").grid(column=1, row=2, sticky=E)
        radio0 = ttk.Radiobutton(self.ruutu, text="oma",
                                variable=self.algoritmiToteutus,
                                value=0
                                )
        radio0.grid(column=2, row=2, sticky=W)
        radio1 = ttk.Radiobutton(self.ruutu, text="SciPy.IO",
                                variable=self.algoritmiToteutus,
                                value=1
                                )
        radio1.grid(column=3, row=2, sticky=W)
        radio1.invoke()

        ttk.Button(
            self.ruutu,
            text="Hae data",
            command=lambda: self._hae_data()
            ).grid(column=3, row=3, sticky=W)

        kuvaaja = Figure(figsize = (10, 3), dpi = 100)
        self.taulu = kuvaaja.add_subplot() 
        
        self.kuvaajaTk = FigureCanvasTkAgg(figure=kuvaaja, master=self.ruutu)
        self.kuvaajaTk.draw()
        toolbar = NavigationToolbar2Tk(self.kuvaajaTk, self.ruutu, pack_toolbar=False)
        toolbar.update()
        self.kuvaajaTk.get_tk_widget().grid(column=0, row=4, columnspan=30, sticky=S)
        toolbar.grid(column=0, row=5, columnspan=30, sticky=N)

        syotteenTarkistaja = (self.ruutu.register(self._tarkista_syote_on_numero), '%P')
        ttk.Label(self.ruutu, text="Valitse poistettava kohta:").grid(column=1, row=6, sticky=E)
        self.kohta = StringVar(value=1)
        ttk.Entry(
            self.ruutu,
            textvariable=self.kohta,
            validate='key',
            validatecommand=syotteenTarkistaja
            ).grid(column=2,row=6, sticky=W)

        ttk.Label(self.ruutu, text="Valitse poiston leveys:").grid(column=1, row=7, sticky=E)
        self.leveys = StringVar(value=1)
        ttk.Entry(
            self.ruutu,
            textvariable=self.leveys,
            validate='key',
            validatecommand=syotteenTarkistaja
            ).grid(column=2,row=7, sticky=W)

        ttk.Button(
            self.ruutu,
            text="Päivitä näkymä",
            command=lambda: self._paivita_kuvaaja()
            ).grid(column=3, row=6, sticky=W)

        ttk.Button(
            self.ruutu,
            text="Poista data kohdasta",
            command=lambda: self._poista_kohta()
            ).grid(column=4, row=6, sticky=W)
        
        ttk.Button(
            self.ruutu,
            text="Tallenna tiedosto",
            command=lambda: self._tallenna_tiedosto()
            ).grid(column=8, row=6, sticky=W)

        for lapsi in self.ruutu.winfo_children(): 
            lapsi.grid_configure(padx=5, pady=5)

        tiedosto_syote.focus()
    
    # TODO siirrä tiedostojenhallinta.py moduuliin _valitse_tiedosto
    def _valitse_tiedosto(self, sijainti, teksti):
        dir = cwd() + "/Syotteet/"
        tiedosto = filedialog.askopenfilename(initialdir=dir, filetypes=[('Audio',['*.wav'])])
        sijainti.set(tiedosto)
        i = tiedosto.rfind("/")
        if i != -1:
            tiedosto = tiedosto[i+1: ]

        teksti.config(text=tiedosto)

    def _tarkista_syote_on_numero(self, syote):
        return re.match('^[0-9]*$', syote) is not None

    def _paivita_kuvaaja(self):
        if self.nykyinenData is not None:
            self.taulu.clear()
            self.taulu.plot(abs(self.nykyinenData[:int(len(self.nykyinenData)/2)]),'r')
            self.taulu.axvline(x=int(self.kohta.get())).set_color('b')
            relatiivinenLeveysMin = int(self.kohta.get())-int(self.leveys.get())
            relatiivinenLeveysMax = int(self.kohta.get())+int(self.leveys.get())
            self.taulu.axvspan(
                xmin=relatiivinenLeveysMin,
                xmax=relatiivinenLeveysMax,
                **{'alpha':0.5})
            self.kuvaajaTk.draw()

    def _poista_kohta(self):
        if self.nykyinenData is not None:
            self.nykyinenData = muokkaus.poista_signaali(
                fftData=self.nykyinenData,
                poistoKohta=int(self.kohta.get()),
                poistoLeveys=int(self.leveys.get())
                )
            self._paivita_kuvaaja()

    def _hae_data(self):
        if self.tiedosto.get() != "":
            if self.algoritmiToteutus.get() == 0:
                omaToteutus = True
            else:
                omaToteutus = False
            data = tiedostojenhallinta.lue_wav_tiedosto(self.tiedosto.get())
            self.otostiheys = data[0]
            self.nykyinenData = data[1]
            self.nykyinenData = algoritmi.suorita_FFT_datalle(self.nykyinenData, omaToteutus)

            self._paivita_kuvaaja()

    def _tallenna_tiedosto(self):
        if self.nykyinenData is not None:
            dir = cwd() + "/Tulosteet/"
            polku = filedialog.asksaveasfilename(initialdir=dir, filetypes=[('Audio',['*.wav'])])
            tiedostojenhallinta.tallenna_tiedosto(
                polku, 
                algoritmi.suorita_iFFT_datalle(self.nykyinenData), 
                self.otostiheys
                )

    def vaihda_ruutuun(self):
        self.ruutu.tkraise()

class voimakkaimmanpoisto:
    def __init__(self, ikkuna=Tk):
        self.nykyinenData = None

        self.ruutu = ttk.Frame(ikkuna)
        self.ruutu.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(self.ruutu, text="Valitse tiedosto:").grid(column=1, row=1, sticky=E)
        self.tiedosto = StringVar()
        tiedosto_teksti = ttk.Label(self.ruutu, text="")
        tiedosto_teksti.grid(column=3, row=1, sticky=E)

        tiedosto_syote = ttk.Button(
            self.ruutu,
            text="Selaa:",
            command=lambda: self._valitse_tiedosto(sijainti=self.tiedosto, teksti=tiedosto_teksti))
        tiedosto_syote.grid(column=2, row=1, sticky=(W, E))
        
        self.algoritmiToteutus = IntVar(value=1)
        ttk.Label(self.ruutu, text="Valitse algoritmin toteutus:").grid(column=1, row=2, sticky=E)
        radio0 = ttk.Radiobutton(self.ruutu, text="oma",
                                variable=self.algoritmiToteutus,
                                value=0
                                )
        radio0.grid(column=2, row=2, sticky=W)
        radio1 = ttk.Radiobutton(self.ruutu, text="SciPy.IO",
                                variable=self.algoritmiToteutus,
                                value=1
                                )
        radio1.grid(column=3, row=2, sticky=W)
        radio1.invoke()

        ttk.Button(
            self.ruutu,
            text="Hae data",
            command=lambda: self._hae_data()
            ).grid(column=3, row=3, sticky=W)

        kuvaaja = Figure(figsize = (10, 3), dpi = 100)
        self.taulu = kuvaaja.add_subplot() 
        
        self.kuvaajaTk = FigureCanvasTkAgg(figure=kuvaaja, master=self.ruutu)
        self.kuvaajaTk.draw()
        toolbar = NavigationToolbar2Tk(self.kuvaajaTk, self.ruutu, pack_toolbar=False)
        toolbar.update()
        self.kuvaajaTk.get_tk_widget().grid(column=0, row=4, columnspan=30, sticky=S)
        toolbar.grid(column=0, row=5, columnspan=30, sticky=N)

        syotteenTarkistaja = (self.ruutu.register(self._tarkista_syote_on_numero), '%P')
        ttk.Label(self.ruutu, text="Poistettava kohta:").grid(column=1, row=6, sticky=E)
        self.kohta = StringVar()
        ttk.Label(self.ruutu, textvariable=self.kohta).grid(column=2, row=6, sticky=W)

        ttk.Label(self.ruutu, text="Valitse poiston leveys:").grid(column=1, row=7, sticky=E)
        self.leveys = StringVar(value=1)
        ttk.Entry(
            self.ruutu,
            textvariable=self.leveys,
            validate='key',
            validatecommand=syotteenTarkistaja
            ).grid(column=2,row=7, sticky=W)

        ttk.Button(
            self.ruutu,
            text="Päivitä näkymä",
            command=lambda: self._paivita_kuvaaja()
            ).grid(column=3, row=6, sticky=W)

        ttk.Button(
            self.ruutu,
            text="Poista data kohdasta",
            command=lambda: self._poista_kohta()
            ).grid(column=4, row=6, sticky=W)
        
        ttk.Button(
            self.ruutu,
            text="Tallenna tiedosto",
            command=lambda: self._tallenna_tiedosto()
            ).grid(column=8, row=6, sticky=W)

        for lapsi in self.ruutu.winfo_children(): 
            lapsi.grid_configure(padx=5, pady=5)

        tiedosto_syote.focus()
    
    # TODO siirrä tiedostojenhallinta.py moduuliin _valitse_tiedosto
    def _valitse_tiedosto(self, sijainti, teksti):
        dir = cwd() + "/Syotteet/"
        tiedosto = filedialog.askopenfilename(initialdir=dir, filetypes=[('Audio',['*.wav'])])
        sijainti.set(tiedosto)
        i = tiedosto.rfind("/")
        if i != -1:
            tiedosto = tiedosto[i+1: ]

        teksti.config(text=tiedosto)

    def _tarkista_syote_on_numero(self, syote):
        return re.match('^[0-9]*$', syote) is not None

    def _paivita_kuvaaja(self):
        if self.nykyinenData is not None:
            self.taulu.clear()
            self.taulu.plot(abs(self.nykyinenData[:int(len(self.nykyinenData)/2)]),'r')
            self.kohta.set(muokkaus._voimakkain_signaali(self.nykyinenData))
            self.taulu.axvline(x=int(self.kohta.get())).set_color('b')
            relatiivinenLeveysMin = int(self.kohta.get())-int(self.leveys.get())
            relatiivinenLeveysMax = int(self.kohta.get())+int(self.leveys.get())
            self.taulu.axvspan(
                xmin=relatiivinenLeveysMin,
                xmax=relatiivinenLeveysMax,
                **{'alpha':0.5})
            self.kuvaajaTk.draw()

    def _poista_kohta(self):
        if self.nykyinenData is not None:
            self.nykyinenData = muokkaus.poista_signaali(
                fftData=self.nykyinenData,
                poistoKohta=int(self.kohta.get()),
                poistoLeveys=int(self.leveys.get())
                )
            self._paivita_kuvaaja()

    def _hae_data(self):
        if self.tiedosto.get() != "":
            if self.algoritmiToteutus.get() == 0:
                omaToteutus = True
            else:
                omaToteutus = False
            data = tiedostojenhallinta.lue_wav_tiedosto(self.tiedosto.get())
            self.otostiheys = data[0]
            self.nykyinenData = data[1]
            self.nykyinenData = algoritmi.suorita_FFT_datalle(self.nykyinenData, omaToteutus)

            self.taulu.clear()
            self.taulu.plot(self.nykyinenData[:int(len(self.nykyinenData)/2)],'r')
            self.kuvaajaTk.draw()

    def _tallenna_tiedosto(self):
        if self.nykyinenData is not None:
            dir = cwd() + "/Tulosteet/"
            polku = filedialog.asksaveasfilename(initialdir=dir, filetypes=[('Audio',['*.wav'])])
            tiedostojenhallinta.tallenna_tiedosto(
                polku, 
                algoritmi.suorita_iFFT_datalle(self.nykyinenData), 
                self.otostiheys
                )

    def vaihda_ruutuun(self):
        self.ruutu.tkraise()
