# Find Digits
# Given an integer, for each digit that makes up the integer determine whether it is a divisor.
# Count the number of divisors occurring within the integer.
# Example
# Check whether , and are divisors of . All 3 numbers divide evenly into so return .

def find_digits():                                          # Name and parameter of function
    n=0
    number = input("Enter a number")
    intnum = int(number)
    uzunluk = len(number)

    for x in range(uzunluk):                                # Loop will run in the number of digits
        if int(number[x]) != 0 and intnum % int(number[x]) == 0:    # if digit is not zero and divisor of number
           n+=1                                             # counter will increase
    return n                                                # number of divisor will be returned

print(find_digits())                                        # Calling function
