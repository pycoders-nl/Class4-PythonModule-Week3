veri=input("Bir cumle giriniz:")
veri=veri.lower()
liste=list(veri)
liste=list(set(liste))
liste.sort()
print(liste)


