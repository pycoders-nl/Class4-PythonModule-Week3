
n = int(input('Lutfen Bir Sayi Girniz.....:')) #Listemizin Son Elemanini Belirliyoruz.
liste=list(range(1,n+1))
mukemmel_sayi_listesi=[]

def mukemmel_sayi(sayi):
    toplam=0
    i=sayi-1
    while i>0:
        if (sayi%i==0):
            toplam+=i
        i-=1
    if (toplam==sayi):
        return 1

# print("Liste....:",liste)     #Listeyi Kontrol Edebilirsiniz Buradan

for i in liste:
    if (mukemmel_sayi(i)==1):

        mukemmel_sayi_listesi.append(i)

print('Mukemmel Sayilar Listesi..............=',mukemmel_sayi_listesi)
print('Mukkemmel Sayilar Listesinin Toplami..=',sum(mukemmel_sayi_listesi))


