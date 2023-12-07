from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from os import getcwd as cwd


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 


from Aanenprosessointi_osat import tiedostojenhallinta, algoritmi



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

        self.algoritmiToteutus = IntVar(value=1)
        ttk.Label(self.ruutu, text="Valitse algoritmin toteutus:").grid(column=1, row=4, sticky=E)
        radio0 = ttk.Radiobutton(self.ruutu, text="oma",
                                variable=self.algoritmiToteutus,
                                value=0
                                )
        radio0.grid(column=2, row=4, sticky=W)
        radio1 = ttk.Radiobutton(self.ruutu, text="SciPy.IO",
                                variable=self.algoritmiToteutus,
                                value=1
                                )
        radio1.grid(column=3, row=4, sticky=W)
        radio1.invoke()

        ttk.Button(self.ruutu, text="Prosessoi", command=lambda: self.prosessoi()).grid(column=3, row=5, sticky=W)

        kuvaaja = Figure(figsize = (10, 3), dpi = 100)
        self.taulu = kuvaaja.add_subplot() 
        
        self.kuvaajaTk = FigureCanvasTkAgg(figure=kuvaaja, master=self.ruutu)
        self.kuvaajaTk.draw()
        toolbar = NavigationToolbar2Tk(self.kuvaajaTk, self.ruutu, pack_toolbar=False)
        toolbar.update()
        self.kuvaajaTk.get_tk_widget().grid(column=0, row=6, columnspan=30, sticky=S)
        toolbar.grid(column=0, row=7, columnspan=30, sticky=N)

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
        if self.algoritmiToteutus.get() == 0:
            omaToteutus = True
        else:
            omaToteutus = False
        data = tiedostojenhallinta.lue_wav_tiedosto(self.tiedosto.get())
        data = data[1]
        if self.suoritetaanko_fft.get() == 1:
            data = algoritmi.suorita_FFT_datalle(data, omaToteutus)

        if self.suoritetaanko_ifft.get() == 1:
            data = algoritmi.suorita_iFFT_datalle(data, omaToteutus)

        self.taulu.clear()
        self.taulu.plot(data,'r')
        self.kuvaajaTk.draw()
        print('prosessoitu')
        
    
    def vaihda_ruutuun(self):
        self.ruutu.tkraise()

class vertailuruutu:
    def __init__(self, ikkuna=Tk):
        self.ruutu = ttk.Frame(ikkuna)
        self.ruutu.grid(column=0, row=0, sticky=(N, W, E, S))

        #------------------tiedosto1 valinta
        ttk.Label(self.ruutu, text="Valitse tiedosto:").grid(column=1, row=1, sticky=E)
        self.tiedosto1 = StringVar()
        tiedosto_teksti1 = ttk.Label(self.ruutu, text="")
        tiedosto_teksti1.grid(column=3, row=1, sticky=E)
        tiedosto_syote1 = ttk.Button(
            self.ruutu,
            text="Selaa:",
            command=lambda: self.valitse_tiedosto(sijainti=self.tiedosto1, teksti=tiedosto_teksti1))
        tiedosto_syote1.grid(column=2, row=1, sticky=(W, E))
        
        ttk.Label(self.ruutu, text="Suoritetaan fft").grid(column=1, row=3, sticky=E)
        self.suoritetaanko_fft = IntVar(value=0)
        suoritetaanko_fft_syote = ttk.Checkbutton(
            self.ruutu, width=7, variable=self.suoritetaanko_fft)
        suoritetaanko_fft_syote.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(self.ruutu, text="Suoritetaan ifft").grid(column=1, row=4, sticky=E)
        self.suoritetaanko_ifft = IntVar(value=0)
        suoritetaanko_ifft_syote = ttk.Checkbutton(
            self.ruutu, width=7, variable=self.suoritetaanko_ifft)
        suoritetaanko_ifft_syote.grid(column=2, row=4, sticky=(W, E))

        self.algoritmiToteutus1 = IntVar(value=1)
        ttk.Label(self.ruutu, text="Valitse algoritmin toteutus:").grid(column=1, row=2, sticky=E)
        radio10 = ttk.Radiobutton(self.ruutu, text="oma",
                                variable=self.algoritmiToteutus1,
                                value=0
                                )
        radio10.grid(column=2, row=2, sticky=W)
        radio11 = ttk.Radiobutton(self.ruutu, text="SciPy.IO",
                                variable=self.algoritmiToteutus1,
                                value=1
                                )
        radio11.grid(column=3, row=2, sticky=W)
        radio11.invoke()
        #------------------

        #------------------tiedosto2 valinta
        ttk.Label(self.ruutu, text="Valitse tiedosto:").grid(column=6, row=1, sticky=E)
        self.tiedosto2 = StringVar()
        tiedosto_teksti2 = ttk.Label(self.ruutu, text="")
        tiedosto_teksti2.grid(column=8, row=1, sticky=E)
        tiedosto_syote2 = ttk.Button(
            self.ruutu,
            text="Selaa:",
            command=lambda: self.valitse_tiedosto(sijainti=self.tiedosto2, teksti=tiedosto_teksti2))
        tiedosto_syote2.grid(column=7, row=1, sticky=(W, E))
        
        self.algoritmiToteutus2 = IntVar(value=1)
        ttk.Label(self.ruutu, text="Valitse algoritmin toteutus:").grid(column=6, row=2, sticky=E)
        radio20 = ttk.Radiobutton(self.ruutu, text="oma",
                                variable=self.algoritmiToteutus2,
                                value=0
                                )
        radio20.grid(column=7, row=2, sticky=W)
        radio21 = ttk.Radiobutton(self.ruutu, text="SciPy.IO",
                                variable=self.algoritmiToteutus2,
                                value=1
                                )
        radio21.grid(column=8, row=2, sticky=W)
        radio21.invoke()
        #------------------

        ttk.Button(
            self.ruutu,
            text="Prosessoi",
            command=lambda: self.prosessoi()
            ).grid(column=2, row=5, sticky=W)

        #------------------kuvaajan piirtäminen
        kuvaaja = Figure(figsize = (10, 3), dpi = 100)
        self.taulu = kuvaaja.add_subplot() 
        
        self.kuvaajaTk = FigureCanvasTkAgg(figure=kuvaaja, master=self.ruutu)
        self.kuvaajaTk.draw()
        toolbar = NavigationToolbar2Tk(self.kuvaajaTk, self.ruutu, pack_toolbar=False)
        toolbar.update()
        self.kuvaajaTk.get_tk_widget().grid(column=0, row=6, columnspan=30, sticky=S)
        toolbar.grid(column=0, row=7, columnspan=30, sticky=N)
        #------------------

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
        print("Aloitetaan prosessointi")
        if self.algoritmiToteutus1.get() == 0:
            omaToteutus1 = True
        else:
            omaToteutus1 = False
        
        if self.algoritmiToteutus2.get() == 0:
            omaToteutus2 = True
        else:
            omaToteutus2 = False

        data1 = tiedostojenhallinta.lue_wav_tiedosto(self.tiedosto1.get())
        data1 = data1[1]
        data2 = tiedostojenhallinta.lue_wav_tiedosto(self.tiedosto2.get())
        data2 = data2[1]

        if self.suoritetaanko_fft.get() == 1:
            data1 = algoritmi.suorita_FFT_datalle(data1, omaToteutus1)
            data2 = algoritmi.suorita_FFT_datalle(data2, omaToteutus2)
            print("fft prosessointu")


        if self.suoritetaanko_ifft.get() == 1:
            data1 = algoritmi.suorita_iFFT_datalle(data1, omaToteutus1)
            data2 = algoritmi.suorita_iFFT_datalle(data2, omaToteutus2)
            print("ifft prosessointu")
        self.taulu.clear()
        self.taulu.plot(data1,'r', alpha=0.5)
        self.taulu.plot(data2,'b', alpha=0.5)

        self.kuvaajaTk.draw()
        print('Valmis')
   
    def vaihda_ruutuun(self):
        self.ruutu.tkraise()
