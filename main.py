
def wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna):
    ceny = {
        'lokalna' : {'list': (0, 0, 2), 'paczka': (0, 0, 7)},
        'krajowa' : {'list': (0, 0, 12), 'paczka': (0, 1, 2)},
        'dalekobiezna' : {'list': (0, 0, 20), 'paczka': (0, 2, 1)}
    } #g s k

    galeony, sykle, knuty = ceny[odleglosc][typ]

    if potwierdzenie_odbioru == True:
        knuty += 7

    if specjalna == 'wyjec':
        knuty += 4
    elif specjalna == 'list gonczy':
        sykle += 1

    return {'galeony' : galeony, 'sykle' : sykle, 'knuty' : knuty}

print(wybierz_sowe_zwroc_koszt(True, 'dalekobiezna', 'paczka', 'list gonczy'))