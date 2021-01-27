#!/usr/bin/env python
# coding: utf-8

# # 1-perfect_number.py

# Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
# 
# The smallest perfect number is 6, which is the sum of 1, 2, and 3.
# 
# Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
# 
# Write a function that finds perfect numbers between 1 and 1000. Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.

# In[ ]:


def perfect_number():

    n = int(input("Please enter a positive number: "))
    numbers = list(range(1,n+1))
    
    for i in numbers:
        sum_divisors=0
        for divisor in range(1,i):
            if i%divisor==0:
                sum_divisors+=divisor
        
        if sum_divisors==i:
            print(sum_divisors)
perfect_number()   


# # 2-reading_number.py

# Write a function that outputs the transcription of an input number with two digits.
# 
# Example:
# 
# 28---------------->Twenty Eight

# In[ ]:


tenth=["Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
units=["one","two","three","four","five","six","seven","eight","nine"]
tentonineteen=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]

def number_to_text():

    number=int(input("Plase enter a number between 10 and 99 : "))
    number_unit=number%10
    number_tenth=number//10

    if 9<number<20:
        print("{}".format(tentonineteen[number_unit]))   
        
    elif 19<number<100:
        if number_unit==0:
            print("{}".format(tenth[number_tenth-2]))        
        else:
            print("{} {}".format(tenth[number_tenth-2],units[number_unit-1]) )       
    else:
        print("Please  enter a correct number!")

number_to_text()


# # 3-alphabetical_order.py

# Write a function that takes an input of different words with hyphen (-) in between them and then:
# 
# sorts the words in alphabetical order,
# adds hyphen icon (-) between them,
# gives the output of the sorted words.
# Example:
# 
# Input  >>> green-red-yellow-black-white
# Output >>> black-green-red-white-yellow 

# In[ ]:


def alphabetical_order(words):
    
    list1=list(words.lower().split("-"))
    list1.sort()
    
    return print("-".join(sorted(list1)))              
     
words=input("Please enter a few different words with hyphen (-) in between them : ")
alphabetical_order(words)


# # 4-unique_list.py

# Write a function that filters all the unique(unrepeated) elements of a given list.
# 
# Example:
# 
# Function call: unique_list([1,2,3,3,3,3,4,5,5])
# Output       : [1, 2, 3, 4, 5]

# In[ ]:


def unique_list(LIJST):
    set_list = set(LIJST)
    return print(list(set_list))

unique_list([1,2,3,3,3,3,4,5,5,6,7,7,8,3,3,4,4,4,5,5,5,6,6,6,7])


# # 5-equal_reverse.py

# Write a function that controls the given inputs whether they are equal to their reversed order or not.
# 
# Example:
# 
# Input  >>> madam, tacocat, utrecht 
# Output >>> True, True, False

# In[ ]:


def equal_reverse(words):  
    
    list1 = words.split(",")
    screen=""
    for i in list1:                              
        reversed_i = i[::-1]                  

        if i == reversed_i:                
            screen += ("True, ")
        else:
            screen += ("False, ")              

    return print(screen)


words = input ("Please enter a few words seperated with comma(,) :")
equal_reverse(words)


# # 6-Find Digits.py

# In[6]:


def findDigits(n):
    s = str(n)
    l = []
    c = 0
    for i in s:
        l.append(i)
    for i in l:
        if int(i) == 0:
            pass
        elif n % int(i) == 0:
            c += 1
    return print(c)       

n = int(input("Please enter a number : "))

findDigits(n)


# # 7- Capitalize!

# In[ ]:


name_surname = input("Please enter the name and the surname")
if len(name_surname) <= 1000:
    name,surname = name_surname.split(" ")
    print(name.capitalize()+" "+surname.capitalize())


# In[ ]:


s = input("Please enter the name and the surname")
if len(s) <= 1000:
    
    print(s.title())

