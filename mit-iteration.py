



def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print ('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
    return result

def main():
    x = int(input("Enter a number "))
    p = int(input("Enter a power "))
    iterativePower(x,p)

main()

