def licz_sume(slownik):
    galeon = sum(slownik['galeon'])
    sykl = sum(slownik['sykl'])
    knut = sum(slownik['knut'])

    sykl += knut // 21
    knut = knut % 21

    galeon += sykl // 17
    sykl = sykl % 17

    return {"galeon" : galeon, "sykl" : sykl, "knut" : knut}


slownik = {
    "galeon" : [1, 3, 5],
    "sykl" : [18, 20, 10],
    "knut" : [30, 40, 7]
}

print(licz_sume(slownik))
