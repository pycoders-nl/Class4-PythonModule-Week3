# Write a function that filters all the unique(unrepeated) elements of a given list.

# Example:
# ```
# Function call: unique_list([1, 2, 3, 3, 3, 3, 4, 5, 5])
# Output: [1, 2, 3, 4, 5]
# ```

def unique_list(arr):
    # convert the list into a set and then convert it back to a list
    # When you convert it to a set it wiull get rid of all of the repeating item and when you convert it back to a list you will get the non-repeating or
    # in other words, unique elements in your list.
    return list(set(arr))


print(unique_list([1, 2, 3, 3, 3, 3, 4, 5, 5]))
