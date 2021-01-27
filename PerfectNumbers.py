
from functools import reduce

print ('0 ile hangi sayi arasindaki  mukemmel sayilarin toplamini istiyorsunuz?')
sayi= (input ("Sayiyi giriniz :"))


n =int(sayi)     # ilk toplam 'sum' ile, ikinci toplam 'reduce' fonksiyonu ile calisiyor

print ('Mukemmel Sayilar', list(filter(lambda n: True if  sum(y for y in range (1,n) if n%y==0)==n else False, range(2, n))))
print ('Toplamlari :', sum(list(filter(lambda n: True if  sum(y for y in range (1,n) if n%y==0)==n else False, range(2, n)))))
print ('Toplamlari :', reduce (lambda a,b: a+b, list(filter(lambda n: True if  sum(y for y in range (1,n) if n%y==0)==n else False, range(2, n)))))

"""" filtreleme ile listeden her bir sayi icin, 
kalansiz bolenlerinin toplami sayinin kendisine esit olanlari ayiriyoruz,
iki if calisyor, ilki kalansiz bolenleri seciyor,  ikincisi, her bir sayi icin secilen bolenlerin toplaminin sayinin kendisine esit olanlar ayriliyor
iki range var birisi verilen sayiya kadar 'n',
digeri bolen icin onu da 1'den verilen sayiya kadar, 'y'"""
