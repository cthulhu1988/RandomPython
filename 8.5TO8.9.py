
def main():
    number = input("Enter a number to convert: ")

    for ch in number:
        alphaNum = ch.isalpha()
        if alphaNum:
            ch = ch.lower()
            character = check(ch)
            print(character,end='')
        else:
            print(ch,end='')
def check(ch):
    if ch in "a b c":
        return "2"
    elif ch in 'def':
        return "3"
    elif ch in 'ghi':
        return "4"
    elif ch in 'jkl':
        return "5"
    elif ch in 'mno':
        return "6"
    elif ch in 'pqrs':
        return "7"
    elif ch in 'tuv':
        return "8"
    elif ch in 'wxyz':
        return "9"
    else:
        return "unknown"
    
  
#main()

def main2():
    lines = 0
    words = 0
    
    fileHandle = open("text.txt","r")
    file = fileHandle.readline()
    while file != '':
        lines+=1
        file = file.split()
        for word in file:
            words+=1
        file = fileHandle.readline()
        average = words/lines
    print(average)
        
#main2()

def main3():
    upperCase = 0
    lowerCase = 0
    numDigits = 0
    whiteSpace = 0
    
    fileHandle = open("text.txt","r")
    fileLine = fileHandle.readline()

    while fileLine !='':
        for ch in fileLine:
            if ch.islower():
                lowerCase+=1
            elif ch.isupper():
                upperCase+=1
            elif ch.isalnum():
                numDigits+=1
            elif ch.isspace():
                whiteSpace+=1
            elif ch.isalpha:
                print("character is {}".format(ch))
            else:
                print(ch,"Err")
        fileLine = fileHandle.readline()
    print(upperCase,lowerCase,numDigits,whiteSpace)
    fileHandle.close()
    
#main3()

def main4():
    parse = input("Enter the string to capitalize: ")
    parse = parse.split(".")

    for sentence in parse:
        sentence = sentence.capitalize()
        print(sentence + "." ,end='')

    
#main4()







        
