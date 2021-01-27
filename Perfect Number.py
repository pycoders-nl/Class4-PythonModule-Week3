from functools import reduce

for rakam in range(1, 1000):

    liste = list(range(1, rakam))
    tamBolenler = list(filter(lambda x: rakam % x == 0, liste))

    if len(tamBolenler) > 1:
        toplam = reduce(lambda x, y: x + y, tamBolenler)

        if toplam == rakam:
            print(rakam)
