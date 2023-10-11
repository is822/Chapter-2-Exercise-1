from math import sqrt

def isprime(n):
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True 

    if n % 2 == 0:
        return False  

    for r in range(3, int(sqrt(n)) + 1, 2):
        if n % r == 0:
            return False  
    
    return True  