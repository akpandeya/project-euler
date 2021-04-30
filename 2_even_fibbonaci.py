# Problem 2: Even Fibonaci
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
import functools

@functools.lru_cache()
def fibonacci(n : int) -> int:
    # print(n)
    
    if (n == 1):
        return 1
    elif (n == 2):
        return 2
    else:
        return fibonacci(n-2) + fibonacci(n-1)

@functools.lru_cache()
def calculate(limit):
    n = fibonacci(1)

    total = 0
    i = 1
    condition = n < limit
    while(condition):
        
        if (n % 2 == 0):
            total += n    
        i += 1
        n = fibonacci(i)
        condition = n < limit
        
    return total
    
print(calculate(4000000))