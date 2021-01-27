

Liste3 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',  'Twelve', 'Thirteen', 'Fourteen',  'Fifteen',  'Sixteen', 'Seventeen',  'Eighteen', 'Nineteen']
Liste2 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', '']
Liste = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', '']


def yazi_sayi(number2):
    if 0<= number2 <20:            # sayi 20 ye kadar liste 3 den aliyor, birler basamagini liste2'den, onlar basamagini liste'den aliyor
        return (Liste3[number2])   # sayiyi 10 a bolerek, listeden alacagi 10'lar basamagindaki sayiyi buluyorum,
    elif  19 < number2 <100:        # sayinin 10 a bolumunden kalan ise birler basamigini veriyor, liste2 den aliyor
        return (Liste[(number2 // 10)]+ ' ' + (Liste2[(number2 % 10)]))
    else:
        return ('Lutfen baska rakam giriniz')


print (yazi_sayi(0))     #0-100 arasi sayi girilebilir


