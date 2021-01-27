"""
Write a function that filters all the unique(unrepeated) elements of a given list.
Example:
Function call: unique_list([1,2,3,3,3,3,4,5,5])
Output       : [1, 2, 3, 4, 5]
"""


def unique_list(n):
    print(list(set(n)))     # girilen liste set komutu ile herbir elemanı benzersiz olan kümeye cevrilir ve yazdırılır.


unique_list([1, 2, 3, 3, 3, 3, 4, 5, 5])
