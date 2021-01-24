# Perfect number: Perfect number, a positive integer that is equal to the sum of its proper divisors.
# The smallest perfect number is 6, which is the sum of 1, 2, and 3.
# Other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
# Write a function that finds perfect numbers between 1 and 1000.
# Check perfect numbers between 1 and 1000 and find the sum of them using with reduce and filter functions.

from functools import reduce            # library to use reduce

def topla(x,y):                         # Name and parameters of function
    return  x+y

mylist = []                             # Empty list named mylist
def perfect_numbers(fltrObj):           # Name and parameters of function

    toplam = 0                          # Searching for of Perfect numbers
    for i in range(1, 1000):
        for j in range(1, 1000):
            if (i % j == 0) and (i != j):
                toplam = toplam + j
        if i == toplam:
            mylist.append(i)
            print(i, "is a Perfect number")
        toplam = 0
fltrObj=filter(perfect_numbers, range(1000))    # to filter perfect numbers
perfect_numbers(fltrObj)                        # callinig function
print("Perfect Numbers: ",mylist)
sum_of_perfects = reduce(topla, mylist)         # using reduce command for cumulative result
print("Sum of perfect numbers between 1 and 1000: ",sum_of_perfects)


