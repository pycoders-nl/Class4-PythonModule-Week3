units = ["zero", "one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]
tens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
         "fifteen", "sixteen", "seventeen", "eightteen", "nineteen"]
tenner = ["", "", "twenty", "thirthy", "forty",
          "fifty", "sixty", "seventy", "eightty", "ninety"]


def number_converter(number):
    if number < 10:
        return units[number]
    elif number // 10 == 1:
        return tens[number % 10]
    else:
        return tenner[number//10] + " " + number_converter(number % 10)

print (number_converter(21))