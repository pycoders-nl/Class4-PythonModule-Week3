# ## 2-reading_number.py
# Write a function that outputs the transcription of an input number with two digits.

# Example:
# ```
# 28--------------- -> Twenty Eight
# ```

def read_num(n):
    ones = ['one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen',
             'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['ten', 'twenty', 'thirty', 'forty',
            'fifty', 'sixty', 'seventy', 'eighty', 'ninty']

    word_form = ''
    digits = [int(x) for x in str(n)]
    word_form += tens[digits[0] - 1]
    if digits[1] == 0:
        pass
    elif digits[0] == 1:
        word_form = teens[digits[1] - 1]
    else:
        word_form = word_form + " " + ones[digits[1]-1]

    return "{} ----------------> {}".format(n, word_form)


print(read_num(25))
print(read_num(56))
print(read_num(29))
print(read_num(47))
print(read_num(88))
print(read_num(94))
print(read_num(40))
print(read_num(39))
print(read_num(68))
print(read_num(71))
print(read_num(10))
print(read_num(19))
print(read_num(14))
print(read_num(13))
print(read_num(16))
