from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from os import getcwd as cwd


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 


import aanenprosessointi



class kuvaajaruutu:
    def __init__(self, ikkuna=Tk):
        self.ikkuna = ikkuna
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

        ttk.Label(self.ruutu, text="Suoritetaan ifft").grid(column=1, row=3, sticky=E)
        self.suoritetaanko_ifft = IntVar(value=0)
        suoritetaanko_ifft_syote = ttk.Checkbutton(
            self.ruutu, width=7, variable=self.suoritetaanko_ifft)
        suoritetaanko_ifft_syote.grid(column=2, row=3, sticky=(W, E))

        ttk.Button(self.ruutu, text="Prosessoi", command=lambda: self.prosessoi()).grid(column=3, row=4, sticky=W)

        kuvaaja = Figure(figsize = (10, 3), dpi = 100)
        self.taulu = kuvaaja.add_subplot(111) 
        
        self.kuvaajaTk = FigureCanvasTkAgg(figure=kuvaaja, master=self.ruutu)
        self.kuvaajaTk.draw()
        toolbar = NavigationToolbar2Tk(self.kuvaajaTk, self.ruutu, pack_toolbar=False)
        toolbar.update()
        self.kuvaajaTk.get_tk_widget().grid(column=0, row=5, columnspan=30, sticky=S)
        toolbar.grid(column=0, row=6, columnspan=30, sticky=N)

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
        fftdata = aanenprosessointi.FFT_tiedostolle(self.tiedosto.get(), False)
        self.taulu.clear()
        self.taulu.plot(fftdata,'r')

        self.kuvaajaTk.draw()
        print('prosessoitu')
        
    
    def vaihda_ruutuun(self):
        self.ruutu.tkraise()