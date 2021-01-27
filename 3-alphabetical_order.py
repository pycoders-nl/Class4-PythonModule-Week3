"""
Write a function that takes an input of different words with hyphen (-) in between them and then:

sorts the words in alphabetical order,
adds hyphen icon (-) between them,
gives the output of the sorted words.
Example:

Input  >>> green-red-yellow-black-white
Output >>> black-green-red-white-yellow
"""


def sort_alphabetical_order(text):
    print('-'.join(sorted(text.split('-'))))    # split ile kelimeler ayrılır. Ayrılan kelimeler sorted ile sıralanır
                                                # join ile tekrar biraraya getirilir.


sort_alphabetical_order(input("Kelimeler arasında '-' bırakarak kelimelerinizi yazınız   :"))
