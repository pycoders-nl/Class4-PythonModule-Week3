print("-"*75)
print(str("-") *30 +"CAPITALIZE"+ str("-")*35)
print("-"*75)

def solve(s):                             #solve adinda bir def functionu olusturuyoruz
    a=s.split(" ")                        # verilen degeri bosluktan split ediyoruz.
    b=[]
    for i in a:                           #split edilmis a yi for loop ile gezip
        b.append(i.capitalize())          #her kelimenin bas harfini buyuk yapiyoruz
    return " ".join(b)                    # functionun sonunda kelimelrin arasina bosluk ile return ediyoruz.
print(solve("bulent caliskan"))           #functionu bir deger ile cagiriyoruz.
