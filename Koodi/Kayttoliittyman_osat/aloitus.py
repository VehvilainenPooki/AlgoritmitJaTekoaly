from tkinter import *
from tkinter import ttk

import webbrowser


class aloitusruutu:
    def __init__(self, ikkuna=Tk):
        self.ruutu = ttk.Frame(ikkuna)
        self.ruutu.grid(column=0, row=0, sticky=(N, W, E, S))
        ttk.Label(self.ruutu, text="Kohinanpoistotyökalu").grid(
            column=1, row=1, sticky=N
        )
        ttk.Label(
            self.ruutu,
            text="Ruudun yläreunasta löytyy valikko, josta voit navigoida eri sivuille.",
        ).grid(column=1, row=3, sticky=N)
        ohjeLinkki = ttk.Label(
            self.ruutu,
            text="Ohjeita työkalun käyttöön",
            foreground="blue",
            cursor="hand2",
        )
        ohjeLinkki.grid(column=1, row=5, sticky=S)
        ohjeLinkki.bind("<Button-1>", lambda l: self.kayttoOhje())

        for lapsi in self.ruutu.winfo_children():
            lapsi.grid_configure(padx=50, pady=5)

    def vaihda_ruutuun(self):
        self.ruutu.tkraise()

    def kayttoOhje(self):
        webbrowser.open_new(
            "https://github.com/VehvilainenPooki/AlgoritmitJaTekoaly/blob/main/Dokumentaatio/Käyttöohje.md"
        )
