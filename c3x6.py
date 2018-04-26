# CLA5b BY Isaac Callison, CSCI 1170-007, Due: 09/22/2016, Lab Assitant: Arthur
# PROGRAM ID: ch3x6.py / Magic Dates
# AUTHOR: Isaac Callison
# INSTALLATION:  MTSU
# Remarks: Program takes user input of month, day and year. if multiple of
# month and day equal year then it is a "magic day" otherwise it is not. 

def main():
    month = int(input("Enter month (numeric): "))
    day = int(input("Enter day: " ))
    year = int(input("Enter two digit year: "))
    multiple = (month*day)

    if (multiple == year):
        print("The day is magic")
    elif (multiple != year):
        print("This date is not magic")
    else:
        print("Enter the correct format")

main()