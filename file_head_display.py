file = input("What file would you like to open? ")

my_file = open(file,"r")

line = my_file.readline()
line = line.rstrip("\n")

x = 0
while x < 5:
    print(line)
    line = my_file.readline()
    line = line.rstrip("\n")
    x+=1
