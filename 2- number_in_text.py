# Write a function that gives the reading of entered any two-digit number.
# Example: 28---------------->Twenty Eight

def read_the_numbers(numbers):                          # Name and parameter of funtion
    if len(number) != 2 :                               # Cheking if two digit number is entered
        print("You didnt enter two digit number")
    else:
        if number[0] == "1":                            # To print irregular numbers between 10-19
            if number[1] == "0": print("ten")
            if number[1] == "1": print("eleven")
            if number[1] == "2": print("twelve")
            if number[1] == "3": print("thirteen")
            if number[1] == "4": print("forteen")
            if number[1] == "5": print("fifteen")
            if number[1] == "6": print("sixteen")
            if number[1] == "7": print("seventeen")
            if number[1] == "8": print("eighteen")
            if number[1] == "9": print("nineteen")

        else:
            if number[0]== "2": print("twenty",end=" ")     # To print reading of index 0
            if number[0]== "3": print("thirty",end=" ")
            if number[0]== "4": print("forty",end=" ")
            if number[0]== "5": print("fifty",end=" ")
            if number[0]== "6": print("sixty",end=" ")
            if number[0]== "7": print("seventy",end=" ")
            if number[0]== "8": print("eighty",end=" ")
            if number[0]== "9": print("ninety",end=" ")

            if number[1]== "1": print("one")                # To print reading of index 1
            if number[1]== "2": print("two")
            if number[1]== "3": print("three")
            if number[1]== "4": print("four")
            if number[1]== "5": print("five")
            if number[1]== "6": print("six")
            if number[1]== "7": print("seven")
            if number[1]== "8": print("eight")
            if number[1]== "9": print("nine")

number = input ("Enter two digit numbers: ")
read_the_numbers(number)                                    # Calling Function