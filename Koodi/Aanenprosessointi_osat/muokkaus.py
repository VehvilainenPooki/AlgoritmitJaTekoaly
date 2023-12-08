import numpy as np


def poista_voimakkain_signaali(fftData=np.array, poistoLeveys=int):
    """
    Poistaa FFT prosessoidusta yksi-ulotteisesta datasta voimakkaimman signaalin.

    Muuttujat:
    fftData = fft:llä prosessoitu äänidata
    poistoLeveys = Kuinka monta otosta poistetaan voimakkaimman signaalin kummaltakin puolelta

    : Palauttaa prosessoidun datan
    """
    data = fftData.copy()
    voimakkainKohta = _voimakkain_signaali(data)
    return poista_signaali(data, voimakkainKohta, poistoLeveys)


def _voimakkain_signaali(fftData=np.array):
    """
    Etsii fft datasta voimakkaaimman data pisteen ja palauttaa sen indexin
    """
    voimakkain = 0
    voimakkainKohta = -1
    datanPituus = int(len(fftData) / 2)
    for kohta in range(datanPituus):
        arvo = fftData[kohta]
        if voimakkain < abs(arvo):
            voimakkain = abs(arvo)
            voimakkainKohta = kohta
    return voimakkainKohta


def poista_signaali(fftData=np.array, poistoKohta=int, poistoLeveys=int):
    """
    Asettaa <poistoKohta> muuttujan kohdan ympäriltä <poistoLeveys> muuttujan kokoisen välin nollaksi

    Muuttujat:
    fftData = fft prosessoitu äänidata
    poistoKohta = Kohta, jonka ympäriltä nollataan data
    poistoLeveys = Leveys, joka nollataan poistoKohdan ympäriltä.

    Palauttaa muunnetun fftData taulukon
    """
    datanPituus = len(fftData) - 1
    for i in range(poistoLeveys * 2 + 1):
        kohta = poistoKohta + i - poistoLeveys
        if datanPituus / 2 > kohta and -1 < kohta:
            fftData[kohta] = 0 + 0j
            fftData[datanPituus - kohta] = 0 + 0j

    return fftData
