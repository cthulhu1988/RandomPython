def main():
	file = input("Enter file name: ")
	print()
	file_object = open(file,"r")
	num=0
	line = file_object.readlines()
	list1 =[]
	print("File list2d.txt converted to 2D list:")
	
	for row in line:
		row = row.split() # splits into two-dimensional list
		print(row)
		int_row = []
		for ele in row: # iterates through each element of each line
			int_row.append(int(ele))
		list1.append(int_row)
		
	print()
	test = int(input("Enter an integer of 0 for quit: "))
	while test != 0:
		for row in list1:
			for char in row:
				if char >= test:
					num+=1
		print("There are {} elements larger than {}".format(num,test))
		num = 0
		print()
		test = int(input("Enter an integer of 0 for quit: "))	
		
main()