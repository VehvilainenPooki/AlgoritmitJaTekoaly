from tkinter import *
from tkinter import ttk




class kayttoliittyma:
    def __init__(self, ikkuna):
        ikkuna.title("Kohinanpoistotyökalu")
        ruutu = ttk.Frame(ikkuna)
        ruutu.grid(column=0, row=0, sticky=(N, W, E, S))
        ikkuna.columnconfigure(0, weight=1)
        ikkuna.rowconfigure(0, weight=1)



        meters = StringVar()
        ttk.Label(ruutu, textvariable=meters).grid(column=2, row=2, sticky=(W, E))


        ttk.Label(ruutu, text="Valitse tiedosto:").grid(column=1, row=1, sticky=E)
        tiedosto = StringVar()
        tiedosto_syote = ttk.Entry(ruutu, width=7, textvariable=tiedosto)
        tiedosto_syote.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(ruutu, text="Poistettava taajuus:").grid(column=1, row=2, sticky=E)
        taajuus = StringVar()
        taajuus_syote = ttk.Entry(ruutu, width=7, textvariable=taajuus)
        taajuus_syote.grid(column=2, row=2, sticky=(W, E))
        ttk.Label(ruutu, text="Hz").grid(column=3, row=2, sticky=W)

        ttk.Label(ruutu, text="Voimakkuuden vähennys:").grid(column=1, row=3, sticky=W)
        voimakkuus = StringVar()
        voimakkuus_syote = ttk.Entry(ruutu, width=7, textvariable=voimakkuus)
        voimakkuus_syote.grid(column=2, row=3, sticky=(W, E))
        ttk.Label(ruutu, text="db").grid(column=3, row=3, sticky=W)

        ttk.Button(ruutu, text="Prosessoi", command=self.prosessoi).grid(column=3, row=4, sticky=W)


        for lapsi in ruutu.winfo_children(): 
            lapsi.grid_configure(padx=5, pady=5)

        tiedosto_syote.focus()
        ikkuna.bind("<Return>", self.prosessoi)

    def prosessoi(self, *args):
        print("TODO prosessointi")


ikkuna = Tk()
kayttoliittyma(ikkuna)
ikkuna.mainloop()