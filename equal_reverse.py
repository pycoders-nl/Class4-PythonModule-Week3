def ters():
    giris = input('Lutfen kelimeri virgulle ayirarak giriniz: ')
    ayrilmis = giris.split(',')
    liste1 = []
    for i in ayrilmis:
        if i == i[::-1]:
            liste1.append('True')
        else:
            liste1.append('False')
    return ','.join(liste1)
print(ters())
        