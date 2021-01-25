print("-"*75)
print(str("-") *30 +"EQUAL REVERSE"+ str("-")*27)
print("-"*75)
def equal_reverse():
    word=input("Enter some words to check if they are equal \nto the reverse order of words.Use (,) between them -> ")
    word = word.lower()            # userdan verdigi kelimelerin tersine esit olup olmadigini ogrenmesi icin bazi kelimeler isiyoruz.
    word_split=word.split(",")     # verilen kelimeri kucuk harflere donusturup virgulden split yapiyoruz.
    a=[]                           # bir a bos listesi olusturup for loop unu kullanarak split edilmis kelimeleri
    for i in word_split:           # geziyoruz.eger kelime  tersine esitse "True" deilse "False" ekliyoruz.
        if i==i[::-1]:
            a.append("True")
        else:
            a.append("False")
    return ", ".join(a)             # def functionun sonunda True False larin arasina virgul koyarak return esiyoruz.
print(equal_reverse())              #equal_reverse function cagiriyoruz.