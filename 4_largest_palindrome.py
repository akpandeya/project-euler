def is_palindrome(word):
    length = len(word)
    for i, letter in enumerate(word):
        if (letter != word[length - i - 1]):
            return False
    return True
def largest_n_digit_number(n : int) -> int:
    sum = 0
    for i in range(n):
        sum += 9*10**i
    return sum
def palindrome_product(digits : int, maximum_value) -> int:
    minimum = 10**(digits -1)
    maximum = 10**digits
    product = 1

    for i in range(maximum, minimum, -1):
        for j in range(maximum, minimum, -1):
            new_product = i*j
            if(is_palindrome(str(i*j)) and new_product <= maximum_value):
                
                if (new_product > product):
                    product = new_product
    return product
print(palindrome_product(3, 999999))