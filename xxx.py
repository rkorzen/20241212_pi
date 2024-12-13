def wyswietl_zawartosc_pliku(nazwa_pliku):
    try:
        with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
            zawartosc = plik.read()
            print(f"Zawartość pliku {nazwa_pliku}:")
            print(zawartosc)
    except FileNotFoundError:
        print(f"Błąd: Plik {nazwa_pliku} nie został znaleziony!")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    sciezka_pliku = 'dane/data.txt'  # domyślna ścieżka do pliku
    wyswietl_zawartosc_pliku(sciezka_pliku) 