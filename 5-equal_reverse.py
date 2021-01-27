kelimeler = input("Kelime giriniz:")
kelimeler = kelimeler.lower()
kelimeler = kelimeler.split(",")


def is_palindrome(s):
    return s == s[::-1]


sonuc = []

for kelime in kelimeler:
    ans = is_palindrome(kelime)
    sonuc.append(str(ans))

print(",".join(sonuc))
