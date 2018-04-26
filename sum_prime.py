n = 15
total = 0
count = 0
x = 0

def is_prime(num):
    is_it_prime = True
    if num <=1:
        is_it_prime = False
    for x in range(2,num):
        if num%x == 0:
            is_it_prime = False
    return is_it_prime


while count < n:
    print("count is {}".format(count))
    if is_prime(x):
        total+=x
        print("total in if is {}".format(total))
        count+=1
        print("count in if is {}".format(count))
    x+=1
    print("this x always cycles",x)
    print(".......................")

print(total,"total")
print(count,"count")

