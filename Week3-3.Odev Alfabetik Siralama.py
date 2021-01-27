
def alfabetik_siralama(kelimeler):
    return ("-".join(map(str,sorted(list(kelimeler.split("-"))))))
kelimeler=str(input('lutfen aralarina (-) koyarak 3 kelime giriniz:'))
print(alfabetik_siralama(kelimeler))