"""
$ python cwiczenie_04.py 100 USD
407.40

import sys

sys.argv
pip install requests
r = request.get...
r.json()

"""
import sys
import requests

print("wartosc atrybitu __name__ w pliku cwiczenie_04.py:", __name__)



# # print(kwota, waluta)
# # {'currency': 'real (Brazylia)', 'code': 'BRL', 'mid': 0.6792},
# resp = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/A")
# for kurs in resp.json()[0]["rates"]:
#     if kurs["code"] == waluta:
#         print(round(kurs["mid"] * kwota, 2))
#         break

def get_kurs(waluta):
    resp = requests.get(f"https://api.nbp.pl/api/exchangerates/tables/A")
    for kurs in resp.json()[0]["rates"]:
        if kurs["code"] == waluta:
            return kurs["mid"]
    return None

def przelicz_walute(kwota, waluta):
    kurs = get_kurs(waluta)
    if kurs is None:
        print(f"Nie znaleziono kursu dla waluty {waluta}")
        return None
    return round(kurs * kwota, 2)

if __name__ == "__main__":

    print(sys.argv)
    if len(sys.argv) != 3:
        print("Użycie: python cwiczenie_04.py kwota waluta")
        sys.exit(1)
    kwota = float(sys.argv[1])
    waluta = sys.argv[2]


    print(przelicz_walute(kwota, waluta))

