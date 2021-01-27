def name(a):
    first = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    second = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninty"]
    third = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    ones_digit = a % 10
    tens_digit = a // 10

    if 10 < a < 20:
        index = (a % 10) - 1
        result = third[index]
        print(result)
    else:
        print(second[tens_digit], first[ones_digit])


number = int(input("Enter a number:"))
while True:
    if 1 < len(str(number)) < 3:
        name(number)
        break
    else:
        print("wrong entry,please try again")
        break







