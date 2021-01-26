# 5-equal_reverse.py
# Write a function that controls the given inputs whether they are equal to their reversed order or not.
#
# Example:
#
# Input  >>> madam, tacocat, utrecht
# Output >>> True, True, False


def equal_reverse():
    given_input = input("enter to different words with comma (,) in between:").lower()
    print("Input >>> ", given_input)

    given_input = given_input.replace(" ", "")  # alinan stringin bosluklarini replace kullanarak yok ettim.

    word_list = given_input.split(",")          # virgullerden ayirarak kelimeleri bir listede topladim.

    result = ""                                 # True ve False ifadelerini bir tutmak icin bos bir str assign ettim.

    for word in word_list:                  # kelime listesi uzerinde for dongusu.
        w = ""                              # kelime nin karakterlerini tutmasi icin bos bir str assign ettim.
        right = -1                          # kelimenin son harfinin index ini refere ediyor.
        for character in word:              # kelime harfleri uzerinde for dongusu.
            if character == word[right]:    # simetrikligi kontrol icin ilk harf ile son harfi kontrol ettim.
                right -= 1                  # sagdan bir sonraki harfe gecmek icin index i eksilttim.
                w += character              # karakterleri string olarak topladim.
                if w == word:               # for dan cikinca toplanan karakterler kelimeye esitse.
                    result += "True,"       # palindrom sozcuk ise resulta True ekledim.
            else:
                result += "False,"          # palindrom sozcuk degil ise resulta False ekledim.
                break                       # kelimede buldugu ilk asimetrik harfte icerdeki donguyu kirdim.
    return print("Output >>>", result)      # istenen sonucu yazdirdim ve func.sonlandi.


equal_reverse()                             # I called the function.
