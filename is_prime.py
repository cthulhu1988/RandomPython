def is_prime(num):
    is_it_prime = True
    if num <=1:
        is_it_prime = False
    for x in range(2,num):
        if num%x == 0:
            is_it_prime = False
    return is_it_prime


for x in range(0,50):
    if is_prime(x):
        print(x)
