print("-"*75)
print(str("-") *30 +"PERFECT NUMBER"+ str("-")*31)
print("-"*75)
def perfect_number():                                                        # perfect number adinda bir def function olusturuyoruz.
     while True:                                                            #devamli donecek olan while loop unu yaziyoruz.
        try:                                                                # try except metodu ile sayidan baska bir sey girilirse hata dan kacinmis
                                                                            # ve tekrar loopun basina donuyoruz.
            x = int(input(" Enter a number between 1 and 1000 ? "))         #user dan 1 ile 1000 arasinda bir sayi girmesini istiyoruz.
            if 1 <= x <= 1000 :                                             # eger sayi 1 ile 1000 arasinda olassa else iel tekrar loop un basina yolluyoruz
                divisible_list=[i for i in range(1,x) if x % i == 0 ]       # x e kadar olan sayilarin x e bolunebilenleri listeye aktariyoruz.
                return ("{} is perfect number".format(x) if sum(divisible_list)==x else "{} is not perfect number".format(x))
                                                                            # return ile listedeki sayilarin toplaminin x e esit olup olmadigini denetliyoruz.
            else:                                                            # esit ise x is perfect number deilse x is not perfect number return ediyoruz
                continue
        except:
            continue
print(perfect_number())                                                        # ensonda da perfect_number fonctionu nu cagiriyoruz.