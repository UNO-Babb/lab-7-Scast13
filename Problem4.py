
import math 

def isPrime(p):
    """Returns boolean (True/False) if the value given is prime."""
    if p < 2:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False  # Even numbers (except 2) are not prime

    for div in range(3, int(math.sqrt(p)) + 1, 2):  # Check up to sqrt(p)
        if p % div == 0:
            return False  
      
    return True

def find_nth_prime(n):
    """Finds the nth prime number."""
    count = 0
    num = 1
    while count < n:
        num += 1
        if isPrime(num):
            count += 1
    return num

# Find the 10001st prime number
if __name__ == '__main__':
    print(find_nth_prime(10001)) 
