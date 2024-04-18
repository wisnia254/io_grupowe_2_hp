#Zadanie 5
def waluta_dict_na_str(fundusz):
    nazwy_monet = {1: 'galeon', 2: 'sykl', 3: 'knut'}

    posortowane_klucze = sorted(fundusz.keys(), reverse=False)
    wynik = []
    for klucz in posortowane_klucze:
        if fundusz[klucz] != 0:  # Pomijamy monety o wartości zerowej
            wynik.append(f"{fundusz[klucz]} {nazwy_monet[klucz]}")
    return ', '.join(wynik)

fundusz = {1: 50, 2: 10, 3: 3}
print(waluta_dict_na_str(fundusz))
