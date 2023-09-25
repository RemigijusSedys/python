# parasyti programa, kuri sudeda du skaicius(su funkcijomis)
# 5 + 8  = 13


def ivedimas(txt):
    sk = int(input(f'{txt}=...'))
    return sk

def sumavimas():
    sk1 = ivedimas('pirmas')
    sk2 = ivedimas('antras')
    # suma = ivedimas('pirmas') + ivedimas('antras')
    suma = sk1 + sk2
    # sk = f'{sk1} + {sk2} = {suma}'
    # return sk
    return suma, sk1, sk2

def rezultatas():
    # print(sumavimas())
    suma, a, b = sumavimas()
    # a, b, c = 5, 8, 7
    print(f'{a}+{b}={suma}')
rezultatas()
