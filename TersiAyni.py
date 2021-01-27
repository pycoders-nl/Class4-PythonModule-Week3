
# Write a function that controls the given inputs whether they are equal to their reversed order or not.



def tersiayni(k):
    if k[::-1] == k[::1]:    # k[::-1] girilen kelimenin tam tersidir, k[::] ya da k[::1] ise kelimenin aynisidir, kontrol ediyoruz
       return True             # ayni ise true verir
    else:
       return False

m= input('Kelime giriniz:')
k = (m).lower()

print  (tersiayni(k))



