import functools


def perfect_number(number):
    summary = 0
    for i in range(1, (number//2)+1):
        if number % i == 0:
            summary += i
    return summary


number_list = [*range(1, 1001)]

perfect_numbers = list(
    filter(lambda number: perfect_number(number) == number, number_list))

print(perfect_numbers)
print(functools.reduce(lambda a, b: a+b, perfect_numbers))
