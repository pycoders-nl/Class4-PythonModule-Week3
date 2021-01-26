# 2-reading_number.py
# Write a function that outputs the transcription of an input number with two digits.
# Example:
# 28---------------->Twenty Eight

def reading_number():
    my_dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
               10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
               80: "eighty", 90: "ninety"}  # sayilari ve okunuslarini bir dict. topladim.
    number = int(input("enter a number: ")) # user in girdigi sayiyi intiger a casting ettim.
    second_digit = number % 10              # sayinin ikinci basamagina ulasmak icin 10a bolumunden kalani assign ettim.
    first_digit = number - second_digit     # sayidan son basamagi cikartip 10lar basamagini assign ettim.
    return print(number, "-------------->", my_dict.get(first_digit).capitalize(),
                 my_dict.get(second_digit).capitalize()) # key leri vererek .get metodu kullatarak value leri yazdirdim.


reading_number()                            # I called the function.
