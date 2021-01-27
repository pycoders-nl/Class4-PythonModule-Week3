from functools import reduce


def sayi_mukemmel_mi(sayi):

    toplam = 0

    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i

    if sayi == toplam:
        return True
    else:
        return False


def mukemmel_sayilar_toplami():
    liste = [j for j in range(1000) if j != 0]
    return reduce(lambda i, j: i + j, filter(lambda i: sayi_mukemmel_mi(i) is True, liste))


print(mukemmel_sayilar_toplami())
