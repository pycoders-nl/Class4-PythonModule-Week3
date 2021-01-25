print("-"*75)
print(str("-") *30 +"UNIQUE LIST"+ str("-")*27)
print("-"*75)
def unique_list(x):              # unique_list adinda bir def function olusturuyoruz.
    a=[]                         # unique olan elemanlari atacagimiz bos list olusturuyoruz.
    for i in x:                  # x in icinde birden fazla olan elemanlari a listesine atiyoruz.
        if i not in a:
            a.append(i)
    return "Your list --> {}\nUnique list --> {}".format(x,a) # sonda verilen listeyi ve unique listesini return yapiyoruz.
print(unique_list([1,2,3,3,3,3,4,5,5]))         # unique_list function i bir liste ile cagiriyoruz.