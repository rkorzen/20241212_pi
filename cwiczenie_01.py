raport = "Raport"

produkt_1 = ("chleb", 6.2, 2.5)

# produkt_1 = "chleb"
# cena_1 = 6.2
# waga_1 = 2.5
produkt_2 = ("masło", 12.2, 3)
# produkt_2 = "masło"
# cena_2 = 12.2
# waga_2 = 3


produkt_3 = ("pomarańcze", 19.49, 6.25)

# produkt_3 = "pomarańcze"
# nazwa_3 = produkt_3[0]
# cena_3 = produkt_3[1]
# waga_3 = produkt_3[2]


nazwa_3, cena_3, waga_3 = produkt_3


raport_1 = f"{produkt_1[0]:15} {produkt_1[1]:4.1f} kg  cena: {produkt_1[1] * produkt_1[2]:6.2f} PLN"
raport_2 = f"{produkt_2[0]:15} {produkt_2[1]:4.1f} kg  cena: {produkt_2[1] * produkt_2[2]:6.2f} PLN"
# raport_2 = f"{produkt_2:15} {waga_2:4.1f} kg  cena: {cena_2 * waga_2:6.2f} PLN"
raport_3 = f"{nazwa_3:15} {waga_3:4.1f} kg  cena: {cena_3 * waga_3:6.2f} PLN"

# print(raport)
# print(raport_1)
# print(raport_2)
# print(raport_3)

raport = f"""
{raport}
{raport_1}
{raport_2}
{raport_3}
"""

print(raport)