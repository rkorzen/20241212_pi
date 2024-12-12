raport = "Raport\n"


nazwy = ["chleb", "masło", "pomarańcze"]
ceny = [6.1, 12.2, 19.49]
wagi = [2.5, 3, 6.25]


# for nazwa in nazwy:
#     index = nazwy.index(nazwa)
#     waga = wagi[index]
#     cena = ceny[index]
#     raport += f"{nazwa:15} {waga:4.1f} kg  cena: {cena * waga:6.2f} PLN\n"
# zaznaczamy fragment
# ctrl + /


for nazwa, cena, waga in zip(nazwy, ceny, wagi):
    raport += f"{nazwa:15} {waga:4.1f} kg  cena: {cena * waga:6.2f} PLN\n"

print(raport)