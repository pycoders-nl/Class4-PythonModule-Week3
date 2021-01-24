
kelime = input("kelime girin: ")
baslangıc = len(kelime) - 1

kelime2 = ""
for index in kelime:
    kelime2 += kelime[baslangıc]
    baslangıc -= 1

print(kelime2)
if kelime == kelime2:
    print(True)
else:
    print(False)