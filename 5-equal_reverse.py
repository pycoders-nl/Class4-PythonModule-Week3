# ## 5-equal_reverse.py
# Write a function that controls the given inputs whether they are equal to their reversed order or not.

# Example:
# ```
# Input >> > madam, tacocat, utrecht
# Output >> > True, True, False
# ```


def equal_reverse(*args):
    return list(map(lambda x: True if x == x[::-1] else False, list(args)))


print(equal_reverse('madam', 'tacocat', 'utrecht'))


################### Explanation ######################

def return_true_false(item):
    if item == item[::-1]:  # By writing [::-1], we meant take all of things in our iterable but write it in reverse order  and if it is equal to the initial item return true
        return True
    else:
        return False


def equal_reverse2(*args):
    # Convert the arguments to a list
    list_words = list(args)
    # Iterate through the defined func above and get the result
    result = map(return_true_false, list_words)
    # convert the result to a list and return
    return list(result)


print(equal_reverse2('madam', 'tacocat', 'utrecht'))
