from functools import reduce
"""num=1000
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(sum==num):
    print("%d ve %d arasındaki 'Perfect Number'lar:" %num)"""



Minimum = 1
Maximum = 1000
perfect_numbers=[]

for Number in range(Minimum, Maximum - 1):
    Sum = 0
    for n in range(1, Number - 1):
        if(Number % n == 0):
            Sum = Sum + n

    if(Sum == Number):
        print(" %d " %Number)
        perfect_numbers.append(Sum)

print("sum of perfect_numbers:",sum(perfect_numbers))
