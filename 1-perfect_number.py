"""
Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
Write a function that finds perfect numbers between 1 and 1000.
Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.
"""
perfect_numbers=[]
for i in range(1,1001):
    sum_divisors = 0
    for divisor in range(1, i):
        if i % divisor == 0:
            sum_divisors += divisor

    if sum_divisors == i:
        perfect_numbers.append(sum_divisors)
print("perfect_numbers:",perfect_numbers)
print("Sum of perfect_numbers:",sum(perfect_numbers))