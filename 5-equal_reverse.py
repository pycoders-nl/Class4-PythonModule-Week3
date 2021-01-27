"""
Write a function that controls the given inputs whether they are equal to their reversed order or not.
Example:
Input  >>> madam, tacocat, utrecht
Output >>> True, True, False
"""
"""def equal_reverse(text):
    words = map(lambda x:x.strip(),text.split(','))
    print( [i==i[::-1] for i in words] )

equal_reverse(input())"""


def equal_reverse(text):

    words = text.split(",")
    result = ""
    for x in words:
        r_x = x[::-1]
        if x == r_x:
            result += "True,"
        else:
            result += "False,"
    return print(result)


text = input("Kelimeler arasında ',' bırakarak kelimelerinizi yazınız  :")
equal_reverse(text)
