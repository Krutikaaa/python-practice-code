def is_palindrome():
    num = 12132423
    if num is not str:
        num = str(num)
        reverse = num[::-1]

        if num == reverse:
            print('Palindrome')
        else:
            print('Not Palindrome')

obj = is_palindrome()