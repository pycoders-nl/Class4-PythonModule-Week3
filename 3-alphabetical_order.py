
words = input("Tire ile ayrılmış kelime dizesi girin:")
words = words.lower()
words = [n for n in words.split('-')]

words.sort()
print('-'.join(words))
