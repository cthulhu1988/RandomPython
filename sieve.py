from math import sqrt



def main2():
    for candidate in range(2,100):
        if is_prime(candidate):
            print(candidate)

def is_prime(candidate):
    for witness in range(2, int(sqrt(candidate))+1):
        print("sq root of candidate",int(sqrt(candidate)),"candidate",candidate)
        if candidate % witness == 0:
            return False
    return True
    

main2()

def main():
    x = primes_upto(100)
    print(x)

def primes_upto(limit):
    is_prime=[False]*2 + [True]* (limit-1)
    for n in range(int(limit**.5 + 1.5)):
        print(n)
        if is_prime[n]:
            print(is_prime[n],n)
            for i in range(n*n, limit+1,n):
                print("i is",i)
                is_prime[i] = False
    return [i for i, prime in enumerate(is_prime) if prime]

#main()
