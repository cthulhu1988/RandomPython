def write():
    file = open("write.txt","w")
    
    for num in range(1,100,6):
        num = str(num)
        file.write(num+"\n")
    file.close()
    
    print("Done")


def read():
    file = open("write.txt","r")
    new_file = file.readlines()

    for ch in new_file:
        print(ch)
    file.close()

#write()
read()
