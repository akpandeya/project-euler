import functools
from typing import Generator

@functools.lru_cache()
def is_prime(n : int) -> bool:
    
    for i in range(2, int(n**0.5) + 1):
        if (n%i == 0):
            return False
    
    return True

@functools.lru_cache()
def is_prime_check_reverse(n : int) -> bool:
    
    for i in range(int(n**0.5) + 1, 1, -1):
        if (n%i == 0):
            return False
    
    return True

@functools.lru_cache()
def get_prime_numbers(upper : int) -> Generator:
    yield 2
    
    for n in range(3, upper+1, 2):
        
        if(is_prime(n)):
            yield n

@functools.lru_cache() 
def get_decreasing_prime_number(upper : int) -> Generator:
    
    for n in range(upper, 1, -1):
        if (is_prime(n)):
            yield n

@functools.lru_cache() 
def prime_factors(n : int) -> Generator:
    for i in get_prime_numbers(n):
        
        if (n % i == 0):
            yield i

def get_smallest_prime_factor(n :int):
    for i in prime_factors(n):
        if (n %i == 0):
            return i
        
def get_largest_prime_factor(n: int) -> int:
    factor = get_smallest_prime_factor(n)

    print ("Out", factor)
    condition = True
    while(condition):
        condition = get_smallest_prime_factor(n)
        if (condition):
            if (condition > factor):
                factor = condition
            n = n//condition
            print ("F: ", factor, "n: ", n)
            
    return factor     
print("Largest" , get_largest_prime_factor(101110))