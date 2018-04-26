n = 20


total = 0
count = 0
x = 2

def is_prime(num):
    is_prime = True
		
    for factor in range(2,num):
        #print("factor {} and num {}".format(factor,num))
        if num % factor == 0:
            div = num/factor
            print("{} x {} = {}".format(factor,div,num))
            is_prime = False
    return is_prime


while count < n:
    if is_prime(x):
        total+=x
        count +=1
        #print("total {},count {},x {} innner loop".format(total,count,x))
    x+=1
    #print("x ->",x)
