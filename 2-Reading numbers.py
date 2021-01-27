birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayi1):
    birinci = sayi1 % 10
    ikinci = sayi1 // 10
    return onlar[ikinci] + " " + birler[birinci]


while True:
    sayi = int(input("Sayı:"))
    if sayi < 10 or sayi > 100:
        print("Lütfen iki basamaklı bir sayı giriniz!")
    else:
        print(okunus(sayi))
        break
