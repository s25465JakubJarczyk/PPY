import math

def oblicz_ilosc_opakowan(dlugosc_podlogi, szerokosc_podlogi, dlugosc_paneli, szerokosc_paneli, ilosc_w_paczce):
    pole = szerokosc_podlogi*dlugosc_podlogi*1.1
    pow_panelu = dlugosc_paneli * szerokosc_paneli
    potrzebna_ilosc_paneli = math.ceil(pole/pow_panelu)
    ilosc_opakowan = math.ceil(potrzebna_ilosc_paneli/ilosc_w_paczce)
    return ilosc_opakowan

