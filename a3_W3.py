# 3-alphabetical_order.py
# Write a function that takes an input of different words with hyphen (-) in between them and then:
# sorts the words in alphabetical order,
# adds hyphen icon (-) between them,
# gives the output of the sorted words.
# Example:
# Input  >>> green-red-yellow-black-white
# Output >>> black-green-red-white-yellow

def alphabetical_order():
    word = input("enter to different words with hyphen (-) in between: ").lower()  # inputu kucuk harfe donusturdum.

    word = word.split("-")                      # kelimeleri aradaki cizgilerden bolerek bir listede topladim.

    word = sorted(word)                         # listeyi sort ettim.

    return print("Output >>> ", *word, sep="-") # kelime listesini aralarina cizgi ekleyerek yazdirdim ve func.sonlandi.


alphabetical_order()                            # I called the function.
