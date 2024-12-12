# napisz kod, który umiescisz w osobnym module
# który przyjmie od uzytkownika liczby (o kazda liczbe pyta osobno)
# wypisz ile bylo unikalnych liczb i jaka jest ich średnia

"""
podaj liczba lub enter by zakonczyc: 1
podaj liczba lub enter by zakonczyc: 1
podaj liczba lub enter by zakonczyc: 2
podaj liczba lub enter by zakonczyc:

wyniki to:
unikalnych liczb: 2
srednia: 1.3333333333333333

"""

liczby = []

while True:
    answer = input("podaj liczba lub enter by zakonczyc: ")
    
    if not answer:
        break
        
    liczby.append(int(answer))

print(f"""
wyniki to:
unikalnych liczb: {len(set(liczby))}
srednia: {sum(liczby) / len(liczby)}

""")
