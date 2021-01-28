def cevirici():
    kelimeler = input('Lutfen arasina tire koyarak kelimeler giriniz: ')
    kelimer = kelimeler.lower()
    kelimer1 = sorted(kelimeler.split('-'))
    sonuc ='-'.join(kelimer1)
    return sonuc
print(cevirici())