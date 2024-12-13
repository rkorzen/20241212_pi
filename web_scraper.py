import pandas as pd

def pobierz_tabele_z_www():
    try:
        # Przykład 1: Pobieranie tabeli z Wikipedii (lista największych miast w Polsce)
        url = "https://pl.wikipedia.org/wiki/Miasta_w_Polsce_(statystyki)"
        
        # read_html zwraca listę wszystkich tabel znalezionych na stronie
        tabele = pd.read_html(url)
        
        # Wybieramy pierwszą tabelę (indeks 0)
        df = tabele[0]
        
        print("Pobrane dane z Wikipedii:")
        print(df.head())
        
        # Zapisanie do pliku CSV
        df.to_csv('dane/miasta.csv', index=False, encoding='utf-8')
        print("\nDane zostały zapisane do pliku 'miasta.csv'")

        # Przykład 2: Pobieranie notowań giełdowych z GPW
        url_gpw = "https://www.bankier.pl/gielda/notowania/akcje"
        df_gpw = pd.read_html(url_gpw)[0]
        
        print("\nPobrane dane z GPW:")
        print(df_gpw.head())

    except Exception as e:
        print(f"Wystąpił błąd podczas pobierania danych: {e}")

if __name__ == "__main__":
    pobierz_tabele_z_www() 