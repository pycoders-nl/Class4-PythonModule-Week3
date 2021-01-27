my_list = []
string = input("Enter input")

# green-red-yellow-black-white

my_list = string.split("-")
my_list.sort()

deger = ""
n = len(my_list)
for i in range(n):
    if i == n - 1:
        deger += my_list[i]
    else:
        deger += my_list[i] + "-"

print(deger)


