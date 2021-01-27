"""
Write a function that outputs the transcription of an input number with two digits.
Example:
28--->Twenty Eight
"""


def transcription(number):
    t_numbers = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty',
                 40: 'Fourty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
    if number in t_numbers:
        print(t_numbers[number])
    else:
        print(t_numbers[number-(number % 10)], t_numbers[number % 10])


transcription(int(input('Enter a number:')))
