print("-"*75)
print(str("-") *30 +"ALPHABETICAL ORDER"+ str("-")*27)
print("-"*75)
def alphabetical_order():                                   # alphabetical_order adinda bir function yaziyoruz.
    word=input("Enter some words with a (-) between them  ")# user dan aralarinda - olan kelimeler istiyoruz.
    word=word.lower()                                       # buyuk harf kullaniminin onune gecmek icin harfleri kucultuyoruz.
    word_split=sorted(word.split("-"))                      # yazilan kelimeri - isaretinden split yapip siraliyoruz.
    result= "-".join(word_split)                            #kelimeler arasina join metodu nu kullanarak - ekliyoruz.
    return result                                           # ve result u return yapiyoruz.
print(alphabetical_order())                                 # function u cagiriyoruz.