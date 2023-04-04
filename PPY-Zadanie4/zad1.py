import math

def ilosc_opakowan_paneli(dl_podlogi, szer_podlogi, dl_panela, szer_panela, ilosc_paneli_w_opakowaniu):
    pow_podlogi = dl_podlogi * szer_podlogi
    pow_pomieszczenia = pow_podlogi * 1.1
    pow_panela = dl_panela * szer_panela
    ilosc_paneli = math.ceil(pow_pomieszczenia / pow_panela)
    ilosc_opakowan = math.ceil(ilosc_paneli / ilosc_paneli_w_opakowaniu)
    return ilosc_opakowan

print(ilosc_opakowan_paneli(5, 4, 1, 0.5, 10));