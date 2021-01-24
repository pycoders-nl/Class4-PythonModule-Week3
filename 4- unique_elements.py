# Write a function that filters all the unique(unrepeated) elements of a given list.
# Example:
# Function call: unique_list([1,2,3,3,3,3,4,5,5])
# Output       : [1, 2, 3, 4, 5]

def unique_list(my_list):           # Name and parameter of funtion
    new_list = set(my_list)         # Convert the list to the set data type
    print(list(new_list))           # Convert the set back to list type and print

unique_list([1,2,3,3,3,3,4,5,5])    # Calling Function


