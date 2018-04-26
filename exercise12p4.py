# exercise12p4.py BY Isaac Callison, CSCI 1170-007, Due: 10/13/2016
# PROGRAM ID: exercise12p4.py
# AUTHOR: Isaac Callison
# INSTALLATION: MTSU
# Read a file name which contains the values to read.
# Read the contents using the read function and print the contents
# Close the file
# Reopen the file
# Using a loop, count and print the contents of the file with a line number as shown below
# Make sure you have a main function and there should not be any global variable used.
# Create 2 files as shown below and test your program.

# collects name of file and stores in variable
file_to_open = input("Enter the name of the file: ")
# opens file and stores file object in a variable
file_object = open(file_to_open,"r")
# reads the first line and stores it in read_file
read_file = file_object.readline()
#read_file = read_file.rstrip("\n")
print()
print("The contents of the data file",file_to_open,"are listed below:")
print()
# while not at the end of a file:
while read_file != '':
    read_file = read_file.rstrip("\n")
    print(read_file)
    read_file = file_object.readline()
    

print("closing",file_to_open)
print()
print("==============================")
file_object.close()
print("re-opening text.txt")
print()
reopen_file_object = open(file_to_open,"r")
count=0
for line in reopen_file_object:
    line = line.rstrip("\n")
    count+=1
    print("line",count,line)
    
print()
print("There are",count,"lines in file",file_to_open)
reopen_file_object.close()

print("closing",file_to_open)



 


