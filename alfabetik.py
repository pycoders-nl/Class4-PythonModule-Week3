kelimeler=input("lütfen listemiz için kelimeler giriniz:\n(kelimeler arası işaretleme yapmadan boşluk bırakarak giriniz)")
k=list(kelimeler)

k =kelimeler.split()

k.sort()
print("alfabetik sıraya göre sıralanan kelimeler:")
print(*k, sep = " - ")
