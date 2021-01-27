


#Liste2 = ['Hawaiian', 'Margherita', 'Mushroom', 'Prosciutto', 'Meat Feast', 'Hawaiian', 'Bacon', 'Black Olive Special', 'Sausage', 'Sausage']
#Liste = [1,2,3,3,3,3,4,5,5]

def UniqueLst(x):
    return list(dict.fromkeys(x))

print (UniqueLst([1,2,2,2,3,3,3,3,4,5,5,6,6,7,7,8,8,9,9]))
print (UniqueLst(['Hawaiian', 'Margherita', 'Mushroom', 'Prosciutto', 'Meat Feast', 'Hawaiian', 'Bacon', 'Black Olive Special', 'Sausage', 'Sausage']))
