# OLA113 BY Isaac Callison,  CSCI 1170-007,  Due: 11/17/16
# PROGRAM ID:  percentage.py / The Percentage Problem
# AUTHOR: Isaac Callison
# INSTALLATION:  MTSU
# REMARKS: Read in data as strings, convert to numeric
# add and determine percentage weight of each value.

def main():
	index = 0
	numeric_lines = []
	added_total = 0

	# open, readlines(), close file. 
	file = open("percentage.dat","r")
	lines = file.readlines()
	file.close()
	# convert string values, append to new list. 
	for string in lines:
		new_num = int(string)
		added_total+=new_num
		numeric_lines.append(new_num)
	
	# first column 11 chars wide, second column 7 chars. 
	print("Sum Equals:   {}".format(added_total) )
	for num in numeric_lines:
		if num != 0: # prevent div by zero error
			percentage = format(num/added_total,">7.2%")
		else:
			percentage = format(0,">7.2%")
		print(format(numeric_lines[index],">11d"),percentage)
		index+=1

main()