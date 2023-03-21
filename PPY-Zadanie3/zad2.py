from random import sample
listaMiast = ["Warszawa","Kraków","Wrocław","Łódź","Poznań","Gdańsk","Szczecin","Bydgoszcz","Lublin","Białystok"]


randomCities = sample(listaMiast,10)
for x in randomCities:
    print(x)