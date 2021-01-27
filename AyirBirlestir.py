
# Write a function that takes an input of different words with hyphen (-) in between them and then:

"""sorts the words in alphabetical order,
#adds hyphen icon (-) between them,
#gives the output of the sorted words"""

# bastaki tek stringi '-' kismindan ayiriyoruz, siraliyoruz, sonra '-' ile tekrar tek bir string yapiyoruz

def ayrac(n):
    return ('-'.join(sorted(n.split('-'))))


print  (ayrac('green-red-yellow-black-white-whitk-bladk-reb-greez'))
print  (ayrac('green-red-yellow-black-white'))





