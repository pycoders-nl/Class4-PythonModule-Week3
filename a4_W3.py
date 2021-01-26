# 4-unique_list.py
# Write a function that filters all the unique(unrepeated) elements of a given list.
# Example:
# Function call: unique_list([1,2,3,3,3,3,4,5,5])
# Output       : [1, 2, 3, 4, 5]

def unique_list():
    my_list=[1,2,3,3,3,3,4,5,5]

    unique_list = list(set(my_list))            # verilen liseyi unique olmasi icin once set e, sonra listeye cevirdim.

    return print("Output   :",unique_list)      # istenen listeyi yazdirdim ve func.sonlandi.

unique_list()                                   # I called the function.
