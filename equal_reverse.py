def reverse():
    word = input("type a word. type 1 to exit: ")
    word_list = []
    while True:
        if word != "1":
            word_list.append(word)
            word = input("type a word. type 1 to exit: ")
        else:
            break
    print(word_list)
    palindrom_words = []
    for word in word_list:
        if word == word[::-1]:
            palindrom_words.append(True)
        else:
            palindrom_words.append(False)
    print(palindrom_words)


reverse()
