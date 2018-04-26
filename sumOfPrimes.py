n = 5
total = 0


def is_prime(num):
    if num <= 1:
        is_prime = False
        return is_prime
    is_prime = True
		
    for factor in range(2,num):
        if num % factor == 0:
            is_prime = False
    return is_prime

while n > 0:
    
    if is_prime(n):
        total += n
        print("n is a prime",n)
        print("total",total)
    n -= 1
    
