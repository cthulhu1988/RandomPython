def is_even(num):
    if num % 2 == 0:
        status = True
    else:
        status = False
    return status


number = int(input("Enter a number: "))

if is_even(number) == True:
    print("The number is even")
else:
    print("The number is Odd")

