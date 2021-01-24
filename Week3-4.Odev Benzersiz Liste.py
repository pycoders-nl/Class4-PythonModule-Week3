sayilar=input('Tekraralayan Bircok sayi Giriniz.....:')

liste=list(sayilar)
liste.sort()

print('Tum liste....:',liste)
def fonksiyon_listesi(liste):
    tekli_liste = []
    for i in liste:
        if i not in tekli_liste:
            tekli_liste.append(i)
    print(tekli_liste)


fonksiyon_listesi(liste)