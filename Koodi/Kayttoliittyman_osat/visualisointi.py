from os import getcwd as cwd

from tkinter import (Tk, N, W, S, E, IntVar, StringVar)
from tkinter import ttk
from tkinter import filedialog

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from Aanenprosessointi_osat import tiedostojenhallinta, algoritmi


class Kuvaajaruutu:
    def __init__(self, ikkuna=Tk):
        self.ikkuna = ikkuna
        self.ruutu = ttk.Frame(ikkuna)
        self.ruutu.grid(column=0, row=0, sticky=(N, W, E, S))

        ttk.Label(self.ruutu, text="Valitse tiedosto:").grid(column=1, row=1, sticky=E)
        self.tiedosto = StringVar()
        tiedostoTeksti = ttk.Label(self.ruutu, text="")
        tiedostoTeksti.grid(column=3, row=1, sticky=E)
        tiedostoSyote = ttk.Button(
            self.ruutu,
            text="Selaa:",
            command=lambda: self.valitse_tiedosto(
                sijainti=self.tiedosto, teksti=tiedostoTeksti
            ),
        )
        tiedostoSyote.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self.ruutu, text="Suoritetaan fft").grid(column=1, row=2, sticky=E)
        self.suoritetaankoFFT = IntVar(value=0)
        suoritetaankoFFTsyote = ttk.Checkbutton(
            self.ruutu, width=7, variable=self.suoritetaankoFFT
        )
        suoritetaankoFFTsyote.grid(column=2, row=2, sticky=(W, E))

        ttk.Label(self.ruutu, text="Suoritetaan ifft").grid(column=1, row=3, sticky=E)
        self.suoritetaankoIFFT = IntVar(value=0)
        suoritetaankoIFFTsyote = ttk.Checkbutton(
            self.ruutu, width=7, variable=self.suoritetaankoIFFT
        )
        suoritetaankoIFFTsyote.grid(column=2, row=3, sticky=(W, E))

        self.algoritmiToteutus = IntVar(value=1)
        ttk.Label(self.ruutu, text="Valitse algoritmin toteutus:").grid(
            column=1, row=4, sticky=E
        )
        radio0 = ttk.Radiobutton(
            self.ruutu, text="oma", variable=self.algoritmiToteutus, value=0
        )
        radio0.grid(column=2, row=4, sticky=W)
        radio1 = ttk.Radiobutton(
            self.ruutu, text="SciPy.IO", variable=self.algoritmiToteutus, value=1
        )
        radio1.grid(column=3, row=4, sticky=W)
        radio1.invoke()

        ttk.Button(self.ruutu, text="Prosessoi", command=lambda: self.prosessoi()).grid(
            column=3, row=5, sticky=W
        )

        kuvaaja = Figure(figsize=(10, 3), dpi=100)
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
        directory = cwd() + "/Syotteet/"
        tiedosto = filedialog.askopenfilename(
            initialdir=directory, filetypes=[("Audio", ["*.wav", "*.mp3"])]
        )
        sijainti.set(tiedosto)
        i = tiedosto.rfind("/")
        if i != -1:
            tiedosto = tiedosto[i + 1 :]

        teksti.config(text=tiedosto)

    def prosessoi(self):
        if self.tiedosto.get() != "":
            omaToteutus = self.algoritmiToteutus.get() == 0
            data = tiedostojenhallinta.lue_wav_tiedosto(self.tiedosto.get())
            data = data[1]
            if self.suoritetaankoFFT.get() == 1:
                data = algoritmi.suorita_fft_datalle(data, omaToteutus)

            if self.suoritetaankoIFFT.get() == 1:
                data = algoritmi.suorita_ifft_datalle(data, omaToteutus)

            self.taulu.clear()
            self.taulu.plot(data, "r")
            self.kuvaajaTk.draw()

    def vaihda_ruutuun(self):
        self.ruutu.tkraise()


class Vertailuruutu:
    def __init__(self, ikkuna=Tk):
        self.ruutu = ttk.Frame(ikkuna)
        self.ruutu.grid(column=0, row=0, sticky=(N, W, E, S))

        # ------------------tiedosto1 valinta
        ttk.Label(self.ruutu, text="Valitse tiedosto:").grid(column=1, row=1, sticky=E)
        self.tiedosto1 = StringVar()
        tiedostoTeksti1 = ttk.Label(self.ruutu, text="")
        tiedostoTeksti1.grid(column=3, row=1, sticky=E)
        tiedostoSyote1 = ttk.Button(
            self.ruutu,
            text="Selaa:",
            command=lambda: self.valitse_tiedosto(
                sijainti=self.tiedosto1, teksti=tiedostoTeksti1
            ),
        )
        tiedostoSyote1.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(self.ruutu, text="Suoritetaan fft").grid(column=1, row=3, sticky=E)
        self.suoritetaankoFFT = IntVar(value=0)
        suoritetaankoFFTsyote = ttk.Checkbutton(
            self.ruutu, width=7, variable=self.suoritetaankoFFT
        )
        suoritetaankoFFTsyote.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(self.ruutu, text="Suoritetaan ifft").grid(column=1, row=4, sticky=E)
        self.suoritetaankoIFFT = IntVar(value=0)
        suoritetaankoIFFTsyote = ttk.Checkbutton(
            self.ruutu, width=7, variable=self.suoritetaankoIFFT
        )
        suoritetaankoIFFTsyote.grid(column=2, row=4, sticky=(W, E))

        self.algoritmiToteutus1 = IntVar(value=1)
        ttk.Label(self.ruutu, text="Valitse algoritmin toteutus:").grid(
            column=1, row=2, sticky=E
        )
        radio10 = ttk.Radiobutton(
            self.ruutu, text="oma", variable=self.algoritmiToteutus1, value=0
        )
        radio10.grid(column=2, row=2, sticky=W)
        radio11 = ttk.Radiobutton(
            self.ruutu, text="SciPy.IO", variable=self.algoritmiToteutus1, value=1
        )
        radio11.grid(column=3, row=2, sticky=W)
        radio11.invoke()
        # ------------------

        # ------------------tiedosto2 valinta
        ttk.Label(self.ruutu, text="Valitse tiedosto:").grid(column=6, row=1, sticky=E)
        self.tiedosto2 = StringVar()
        tiedostoTeksti2 = ttk.Label(self.ruutu, text="")
        tiedostoTeksti2.grid(column=8, row=1, sticky=E)
        tiedostoSyote2 = ttk.Button(
            self.ruutu,
            text="Selaa:",
            command=lambda: self.valitse_tiedosto(
                sijainti=self.tiedosto2, teksti=tiedostoTeksti2
            ),
        )
        tiedostoSyote2.grid(column=7, row=1, sticky=(W, E))

        self.algoritmiToteutus2 = IntVar(value=1)
        ttk.Label(self.ruutu, text="Valitse algoritmin toteutus:").grid(
            column=6, row=2, sticky=E
        )
        radio20 = ttk.Radiobutton(
            self.ruutu, text="oma", variable=self.algoritmiToteutus2, value=0
        )
        radio20.grid(column=7, row=2, sticky=W)
        radio21 = ttk.Radiobutton(
            self.ruutu, text="SciPy.IO", variable=self.algoritmiToteutus2, value=1
        )
        radio21.grid(column=8, row=2, sticky=W)
        radio21.invoke()
        # ------------------

        ttk.Button(self.ruutu, text="Prosessoi", command=lambda: self.prosessoi()).grid(
            column=2, row=5, sticky=W
        )

        # ------------------kuvaajan piirtäminen
        kuvaaja = Figure(figsize=(10, 3), dpi=100)
        self.taulu = kuvaaja.add_subplot()

        self.kuvaajaTk = FigureCanvasTkAgg(figure=kuvaaja, master=self.ruutu)
        self.kuvaajaTk.draw()
        toolbar = NavigationToolbar2Tk(self.kuvaajaTk, self.ruutu, pack_toolbar=False)
        toolbar.update()
        self.kuvaajaTk.get_tk_widget().grid(column=0, row=6, columnspan=30, sticky=S)
        toolbar.grid(column=0, row=7, columnspan=30, sticky=N)
        # ------------------

        for lapsi in self.ruutu.winfo_children():
            lapsi.grid_configure(padx=5, pady=5)

    def valitse_tiedosto(self, sijainti, teksti):
        directory = cwd() + "/Syotteet/"
        tiedosto = filedialog.askopenfilename(
            initialdir=directory, filetypes=[("Audio", ["*.wav", "*.mp3"])]
        )
        sijainti.set(tiedosto)
        i = tiedosto.rfind("/")
        if i != -1:
            tiedosto = tiedosto[i + 1 :]

        teksti.config(text=tiedosto)

    def prosessoi(self):
        if self.tiedosto1.get() != "" and self.tiedosto2.get() != "":
            omaToteutus1 = self.algoritmiToteutus1.get() == 0
            omaToteutus2 = self.algoritmiToteutus2.get() == 0
            data1 = tiedostojenhallinta.lue_wav_tiedosto(self.tiedosto1.get())
            data1 = data1[1]
            data2 = tiedostojenhallinta.lue_wav_tiedosto(self.tiedosto2.get())
            data2 = data2[1]

            if self.suoritetaankoFFT.get() == 1:
                data1 = algoritmi.suorita_fft_datalle(data1, omaToteutus1)
                data2 = algoritmi.suorita_fft_datalle(data2, omaToteutus2)
            if self.suoritetaankoIFFT.get() == 1:
                data1 = algoritmi.suorita_ifft_datalle(data1, omaToteutus1)
                data2 = algoritmi.suorita_ifft_datalle(data2, omaToteutus2)

            self.taulu.clear()
            self.taulu.plot(data1, "r", alpha=0.5)
            self.taulu.plot(data2, "b", alpha=0.5)

            self.kuvaajaTk.draw()

    def vaihda_ruutuun(self):
        self.ruutu.tkraise()
