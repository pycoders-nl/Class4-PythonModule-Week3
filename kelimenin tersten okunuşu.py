
sözcük = input("Bir kelime giriniz:")

"""Kullanıcının girdiği kelimedeki büyük harfleri de küçük harf olarak algılaması için:"""

sözcük = sözcük.lower()
l = len(sözcük)
p = l-1
index = 0
while index < p:
    if sözcük[index] == sözcük[p]:
        index = index + 1
        p = p-1

        print("Girdiğiniz kelime, tersten okunuşu ile aynıdır.")
        break
    else:
        print("Girdiğiniz kelime, tersten okunuşu ile aynı değildir.")
        break