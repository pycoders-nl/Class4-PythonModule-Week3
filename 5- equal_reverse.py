# Write a function that controls the given inputs
# whether they are equal to their reversed order or not.
# Example:
# Input  >>> madam, tacocat, utrecht
# Output >>> True, True, False

def palindrom(args):                                # Name and parameter of function
    result=""
    for word in args:                               # list elements will be visited
        reversed_word = word[::-1]                  # will be checked if it is a palindrom

        if word == reversed_word:                   # If palindrom True
            result += ("True, ")
        else:
            result += ("False, ")                   # If not False answer will be returned

    return result
original_word = input ("Enter words seperated with only comma sign ',' :")
mylist = original_word.split(",")
print(palindrom(mylist))                            # Calling function