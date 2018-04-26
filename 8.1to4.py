import time,datetime

def main():
    name = input("Enter your first ,middle and last name: ")
    name = name.split()
    for word in name:
        ch = word[0]
        print(ch+'.',end='')
#main()

def main2():
    count = 0
    numbers = input("Enter a string of numbers to add: ")
    for ch in numbers:
        ch = int(ch)
        count += ch
    print(count)
#main2()

def main3():
    date = input("Input the date in mm/dd/yyyy format: ")
    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:10])
    mydate = datetime.date(year,month,day)
    mydate = mydate.strftime("%A")
    print(mydate)
#main3()

def main4():
    space = ' '
    comma = "--..--"
    period = ".-.-.-"
    queston = "..--.."
    
    string = input("Enter a string: ")
    for ch in string:
        newCh = convert(ch)
        print(newCh + " " ,end='')

def convert(ch):
    if ch == '0':
        return '-----'
    elif ch == '1':
        return '.----'
    elif ch == '2':
        return '..---'
    elif ch == '3':
        return '...--'
    elif ch == '4':
        return '....-'
    elif ch == '5':
        return '.....'
    elif ch == '6':
        return '-....'
    elif ch == '7':
        return '--...'
    elif ch == '8':
        return '---..'
    elif ch == '9':
        return '----.'
    elif ch == 'a':
        return '.-'
    elif ch == 'b':
        return '-...'
    elif ch == 'c':
        return '-.-.'
    elif ch == 'd':
        return '-..'
    elif ch == 'e':
        return '.'
    elif ch == 'f':
        return '..-.'
    elif ch == 'g':
        return '--.'
    elif ch == 'h':
        return '....'
    elif ch == 'i':
        return '..'
    elif ch == 'j':
        return '.---'
    elif ch == 'k':
        return '-.-'
    elif ch == 'l':
        return '.-..'
    elif ch == 'm':
        return '--'
    elif ch == 'n':
        return '-.'
    elif ch == 'o':
        return '---'
    elif ch == 'p':
        return '.--.'
    elif ch == 'q':
        return '--.-'
    elif ch == 'r':
        return '.-.'
    elif ch == 's':
        return '...'
    elif ch == 't':
        return '-'
    elif ch == 'u':
        return '..-'
    elif ch == 'v':
        return '...-'
    elif ch == 'w':
        return '.--'
    elif ch == 'x':
        return '-..-'
    elif ch == 'y':
        return '-.-'
    elif ch == 'z':
        return '--..'
    elif ch == ' ':
        return ' * '
    elif ch == ',':
        return '--..--'
    elif ch == '.':
        return '.-.-.-'
    elif ch == '?':
        return '..--..'
    else:
        return "Unknown"


    
main4()
