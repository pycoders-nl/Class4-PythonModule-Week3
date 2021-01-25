print("-"*75)
print(str("-") *30 +"READING NUMBER"+ str("-")*31)
print("-"*75)
def reading_number():                                                                                                   # reading number adinda bir def function  tanimliyoruz.
    while True:                                                                                                         # programdan cikilmadigi takdirde donen bir while loop u yaziyoruz
        try:                                                                                                            # yanlis inputlardan kacinmak icin try except metodunu kullaniyoruz.
            x=input("Enter a two digit number ? ")                                                                      #user dan iki basamakli bir sayi girmesini istiyoruz ve x variable ina atiyotuz.
            if len(x)==2:                                                                                               # if else ile sayinin iki basamakli olup olmadigina bakiyoruz.Deilse loop un basina yolluyoruz.
                ones_digit=["","one","two","three","four","five","six","seven","eight","nine"]                           # verecegimiz outputlari 3 liste seklinde hazirliyoruz.
                tens_digit=["","Ten","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
                decimals=["","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
                if x[1]=="0":                                                                                           # eger x sayisinin birler basamagi 0 ise girecek if statment yaziyoruz.
                    a= [i for i in tens_digit if int(x[0])== tens_digit.index(i)]                                       # for ile tens_digit listesini geziyoruz ve eger x in onlar basamagi
                    return  "{} ---------> {}".format(x,a[0])                                                           #tens_digit deki br elemanin index ine esitse print olmasi gereken ifadeyi return yapiyoruz.
                elif x[0]=="1":                                                                                         #eger x sayisinin onlar basamagi 1 ise girecek if statment yaziyoruz.
                    a=[i for i in decimals if int(x[1])== decimals.index(i)]                                            #for ile decimals listesini geziyoruz ve eger x in birler basamagi
                    return "{} ---------> {}".format(x,a[0])                                                            #decimal  deki br elemanin index ine esitse print olmasi gereken ifadeyi return yapiyoruz.
                else:
                    last1=[i for i in tens_digit if int(x[0])==tens_digit.index(i)]                                     # ilk iki ifade calismassa else stament calisir.burada last1 ve
                    last2=[i for i in ones_digit if int(x[1])== ones_digit.index(i)]                                    #last2 listesini yukarda anlatilan gibi olusturuyoruz.
                    return "{} ---------> {}-{}".format(x, last1[0], last2[0])                                          # ve return olmasi gereken ifadeyi return ediyoruz.
            else:
                print("You did not enter two digit number! ")
                continue
        except:
            print("You did not enter two digit number! ")
            continue

print(reading_number())