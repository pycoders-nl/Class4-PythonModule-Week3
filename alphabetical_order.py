def sorter():

    word = input("type a word. type 1 to exit: ")
    word_list = []
    while True:
        if word != "1":
            word_list.append(word)
            word = input("type a word. type 1 to exit: ")
        else:
            break
    sorted_list = ("-").join(word_list)
    print(sorted_list)
    result = ("-").join(sorted(word_list))
    print(result)

sorter()
