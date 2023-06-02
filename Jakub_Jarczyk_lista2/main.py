import ssl
import pandas as pd
from sklearn import preprocessing
import sqlite3
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, LeaveOneOut

ssl._create_default_https_context = ssl._create_unverified_context

# Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
# do ramki danych.
# Użyj reszty wierszy jako nagłówków ramki danych.
# Uwaga! Zobacz która zmienna jest zmienną objaśnianą, będzie to potrzebne do dalszych zadań.

path = "pliktextowy.txt"
file1 = open(path, 'r')
Lines = file1.read().splitlines()
url = Lines[0]
head = Lines[1:]
df = pd.read_csv(url, names=head)

# Zadanie1 przypisz nazwy kolumn z df w jednej linii:   (2pkt)

wynik1 = ""
for line in Lines[1:]:
    wynik1 += f"{line} "
print(wynik1)

# Zadanie 2: Wypisz liczbę wierszy oraz kolumn ramki danych w jednej linii.  (2pkt)
wynik2 = f"Columns: {len(df.columns)}, Rows: {len(df.index)}"
print(wynik2)


# Zadanie Utwórz klasę Wine na podstawie wczytanego zbioru:
# wszystkie zmienne objaśniające powinny być w liscie.
# Zmienna objaśniana jako odrębne pole.
# metoda __init__ powinna posiadać 2 parametry:
# listę (zmienne objaśniające) oraz liczbę(zmienna objaśniana).
# nazwy mogą być dowolne.

# Klasa powinna umożliwiać stworzenie nowego obiektu na podstawie
# już istniejącego obiektu jak w pdf z lekcji lab6.
# podpowiedź: metoda magiczna __repr__
# Nie pisz metody __str__.

# Zadanie 3 Utwórz przykładowy obiekt:   (3pkt)
class Wine:
    def __init__(self, list, liczb):
        self.list = list
        self.liczb = liczb

    def __repr__(self):
        return f"Wine(list={self.list}, liczb={self.liczb})"


wynik3 = Wine(list=df.iloc[0][1:].tolist(), liczb=int(df.iloc[0][0]))
# do podmiany. Pamiętaj - ilość elementów, jak w zbiorze danych.
# Uwaga! Pamiętaj, która zmienna jest zmienną objaśnianą
print(wynik3)

# Zadanie 4.                             (3pkt)
# Zapisz wszystkie dane z ramki danych do listy obiektów typu Wine.
# Nie podmieniaj listy, dodawaj elementy.
# Uwaga! zobacz w jakiej kolejności podawane są zmienne objaśniające i objaśniana.
# Podpowiedź zobacz w pliktextowy.txt
wineList = []
for elem in df.iloc:
    wineList.append(Wine(list=elem[1:].tolist(), liczb=int(elem[0])))
wynik4 = len(wineList)
print(wynik4)

# Zadanie5 - Weź ostatni element z listy i na podstawie         (3pkt)
# wyniku funkcji repr utwórz nowy obiekt - eval(repr(obiekt))
# do wyniku przypisz zmienną objaśnianą z tego obiektu:


wynik5 = eval(repr(wineList[-1]))
print(wynik5)

# Zadanie 6:                                                          (3pkt)
# Zapisz ramkę danych  do bazy SQLite nazwa bazy(dopisz swoje imię i nazwisko):
# wines_imie_nazwisko, nazwa tabeli: wines.
# Następnie wczytaj dane z tabeli wybierając z bazy danych tylko wiersze z typem wina nr 3
# i zapisz je do nowego data frame:

conn = sqlite3.connect('wines_Kamil_Kłodawski.db')
conn.execute('''CREATE TABLE IF NOT EXISTS wines
                (liczb int,
                list text);
            ''')

conn.execute("DELETE FROM wines")
for elem in wineList:
    conn.execute(f'''INSERT INTO wines VALUES
                ({elem.liczb}, '{elem.list}')
              ''')
conn.commit()

res = conn.cursor().execute("SELECT * FROM wines WHERE liczb = 3").fetchall()
sqlWines = []
for elem in res:
    listt = []
    listt.append(elem[0])
    ll = [float(x) for x in elem[1][1:-1].split(', ')]
    for x in ll:
      listt.append(x)
    sqlWines.append(listt)
conn.close()
wynik6 = "W następnej linijce podmień na nowy  data frame z winami tylko klasy trzeciej:"
wynik6 = pd.DataFrame(sqlWines,columns=Lines[1:])

print(wynik6.shape)

# Zadanie 7                                                          (1pkt)
# Utwórz model regresji Logistycznej z domyślnymi ustawieniami:

model = LogisticRegression()

wynik7 = model.__class__.__name__
print(wynik7)

# Zadanie 8:                                                        (3pkt)
# Dokonaj podziału ramki danych na dane objaśniające i  do klasyfikacji.
# Znormalizuj dane objaśniające za pomocą:
# X = preprocessing.normalize(X)
# Wytenuj model na wszystkich danych bez podziału na zbiór treningowy i testowy.
# Wykonaj sprawdzian krzyżowy, używając LeaveOneOut() zamiast KFold (Parametr cv)
#  Podaj średnią dokładność (accuracy)
X = df.iloc[:,1:]
y = df.iloc[:,0]

X = preprocessing.normalize(X)

acc = cross_val_score(model,X,y,cv=LeaveOneOut())

wynik8 = acc.mean()
print(wynik8)
