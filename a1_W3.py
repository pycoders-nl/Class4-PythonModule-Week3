from functools import reduce

# 1-perfect_number.py
# Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
# The smallest perfect number is 6, which is the sum of 1, 2, and 3.
# Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
# Write a function that finds perfect numbers between 1 and 1000.
# Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.

def perfect_number():
    my_list = [*range(1, 1000)]                     # istenen aralikta bir sayi listesi olusturdum.
    perfect_num = []                                # perfect sayilari tutmak icin bos bir liste.
    for i in range(1, 1000):                        # ayni sayi araliginda for ile dolastim.
        result = list(filter(lambda x: i > x and i % x == 0, my_list))
        # lambda func.ile listeden alinan bir sayi kendinden kucuk sayilardan hangisine tam boluyor ise filtreledim.
        if not result:                              # result listesi bos ise devam et dedim.
            continue
        summ = reduce(lambda a, b: a + b, result)   # reduce func. ile result listesindeki sayilari topladim.
        if summ == i: # perfect sartini kontrol ettim.
            perfect_num.append(i)                   # sayi perfect ise listeye ekledim.
    print("Perfect Numbers:")
    return print(*perfect_num, sep=",")             # istenen sonucu yazdirdim ve func.sonlandi.

perfect_number()                                    # I called the function.




# my another solution:
# perfect_number=[]
# for i in range(1,1000):
#     result=0
#     for j in range(1,i+1):
#         if i%j==0:
#             result+=j
#             if result == i:
#                 perfect_number.append(i)
# print(perfect_number)
