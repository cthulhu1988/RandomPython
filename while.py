def main():

    keep_going = "y"



    while keep_going == "y":
        sales = float(input("Enter amount of sales: "))

        com_rate = float(input("Enter commission rate: "))

        commision = sales* com_rate

        print("the commision is",commision)

        keep_going = input("do you want another? y or n ")
    
main()
