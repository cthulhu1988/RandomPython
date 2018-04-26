import random as r
num = r.randint(1,100)
#print(num)


def is_it_prime(num):
    is_prime = True
		
    for factor in range(2,num):
        if num % factor == 0:
            is_prime = False
    print(num,is_prime)

#is_it_prime(num)


while num!= 10:
    num = r.randint(1,10)
    is_it_prime(num)
    
    
