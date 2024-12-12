import sys

if len(sys.argv) < 2:
    print("Poprawne wywołanie to: python sumator.py n")
    print("gdzie n to przynajmniej 1 liczba")
    exit()

data = sys.argv[1:]
print(data)

# suma = 0
# for liczba in data:
#     suma += int(liczba)

# print(suma)

# print(map(int, data))
# print(list(map(int, data)))

print(sum(map(int, data)))

