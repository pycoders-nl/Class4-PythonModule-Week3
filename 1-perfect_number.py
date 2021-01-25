# ## 1-perfect_number.py
# Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.

# The smallest perfect number is `6`, which is the sum of `1`, `2`, and `3`.

# Some other perfect numbers are `28(1+2+4+7+14=28)`, `496` and `8128`.

# Write a function that finds perfect numbers between `1` and `1000`.
# Check perfect numbers between `1` and `1000` and find the sum of the perfect numbers using reduce and filter functions.

from functools import reduce

############# METHOD 1 #############


def perfect_numbers(num=1000):
    for i in range(1, num + 1):
        divisors = list(filter(lambda x: i % x == 0, range(1, (i // 2 + 1))))
        if len(divisors) > 1:
            sum_divisors = reduce(lambda x, y: x+y, divisors)
            if sum_divisors == i:
                print("{} is a perfect number".format(i))


perfect_numbers()

############# METHOD 2 #############


def perfect_numbers2(num=1000):
    for i in range(1, num + 1):
        sum = 0
        for j in range(1, int(i // 2) + 1):
            if i % j == 0:
                sum += j

        if sum == i:
            print("{} is a perfect number".format(sum))


perfect_numbers2()
