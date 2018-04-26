def main():

    file_object = open("text.txt","r")

    file = file_object.readline()

    file = file.rstrip("\n")

    while file != '':
        print(file)
        file = file_object.readline()
        file = file.rstrip('\n')

    file_object.close()
    print("done")



#main()
    
def main2():

    file_object = open("text.txt","r")

    for line in file_object:
        line = line.rstrip("\n")

        print(line)

    file_object.close()
    print("done")



main2()
