with open("dane/data.txt") as f:
    for line in f:
        if line.startswith("The document was modified on "):
            # print(line.split())
            # print(line.split()[-1])
            # print(line.split()[-1][:-1])
            # print(line.split()[-1].replace(".",""))

            lista = line.split()
            ostatni_element = lista[-1]
            text_bez_kropki = ostatni_element.replace(".", "")
            print(text_bez_kropki)
