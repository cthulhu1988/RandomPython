def main():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    id_number = input("Please enter your ID number: ")

    if len(first_name) < 4:
        first_portion = first_name
    else:
        first_portion = first_name[0:3]

    if len(last_name) < 4:
        middle_portion = last_name
    else:
        middle_portion = last_name[0:3]
    if len(id_number) < 4:
        last_portion = id_number
    else:
        last_portion = id_number[-3:]

    print("Your new number is: ",first_portion,middle_portion,last_portion,sep='')
main()
