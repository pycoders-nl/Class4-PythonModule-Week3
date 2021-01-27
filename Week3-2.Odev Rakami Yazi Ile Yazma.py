
sayi=int(input('Iki Basamakli Bir Sayi Giriniz...:'))

def yazi (a):
    birler=['','Bir','Iki','Uc','Dort','Bes','Alti','Yedi','Sekiz','Dokuz']
    onlar=['','On','Yirmi','Otuz','Kirk','Elli','Altmis','Yetmis','Seksen','Doksan']
    bir=a%10
    on =a//10
    print(onlar[on],birler[bir])

sayac=1
while sayac==1:
    if 10<=sayi<=99:
        print('Girdiginiz Rakam Iki Basamakli Sonuc Assagidadir.....')
        yazi(sayi)

        sayac=0
    else:
        print('DIKKAT ,Yanlis Girdiniz Lutfen Iki Basanakli Sayi Giriniz.....')
        sayi=int(input('Iki Basamakli Sayi Giriniz...:'))







