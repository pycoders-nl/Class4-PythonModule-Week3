# Write a function that takes an input form user which separates the words hyphen icon(-) and
# sort the words alphabetical order and then adds hyphen icon (-) between them and gives the output of it.
# Example:
#
# Input  >>> green-red-yellow-black-white
# Output >>> black-green-red-white-yellow

def alphatebic_order(sentence):         # Name and parameter of funtion
    mylist = sentence.split("-")        # decompose the string an put into the elements in mylist
    print("-".join(sorted(mylist)))     # join them in a new string in a sorted form

sentence = input ("Enter a sentence with '-' sign between words: ")
alphatebic_order(sentence)              # Calling function


