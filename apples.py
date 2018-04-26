x = int(input("How many apples are you taking: "))

while x != 4:

    if x < 5:
        print("You have chosen too few")
        print()
        x = int(input("How many apples are you taking: "))
    elif x >= 5:
        print("You have chosen too many")
        print()
        x = int(input("How many apples are you taking: "))
    
print("Just the right amount")


