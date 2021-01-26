# Write a function that filters all the unique(unrepeated) elements of a given list.

# Example:

# Function call: unique_list([1,2,3,3,3,3,4,5,5])
# Output       : [1, 2, 3, 4, 5]

def unique_list(given_list): # Takes a list as argument
    return list(set(given_list)) # Makes a set with unique elements then makes a list

print(unique_list([1,2,3,3,3,3,4,5,5]))

