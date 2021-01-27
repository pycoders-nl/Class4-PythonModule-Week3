def perfect_number(*args):
    a = 0
    x = []
    giris = int(input('Please enter the number: '))
    for i in range(1, giris + 1):
        if giris % i == 0:
            a = a + i
            if a == giris:
                print('You found the perfect number', giris)

perfect_number()
# for i in range(1, 1001):
#
