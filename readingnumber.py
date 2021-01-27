onluk = {1:'on', 2:'yirmi', 3:'otuz', 4:'kirk', 5:'elli', 6:'altmis', 7:'yetmois', 8:'seksen', 9:'doksan'}
birlik = {0:'', 1:'bir', 2:'iki', 3:'uc', 4:'dort', 5:'bes', 6:'alti', 7:'yedi', 8:'sekiz', 9:'dokuz'}
sayi = input('Lutfen 2 basamakli sayi giriniz: ')

a = int(sayi[0])
b = int(sayi[1])

print(onluk[(a)] + birlik[(b)])