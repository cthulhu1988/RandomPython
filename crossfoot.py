



def check_digit(num):
	remnant = num # remnant = 61248 num = 61248
	cross_foot = 0 # set at 0
	
	while remnant > 0: #should cycle
		last_digit = (remnant % 10) # is 8
		product = (last_digit*2) # is 16
		last_dig_product = product % 10 # should be 6
		first_dig_product = product // 10 # cut off 6 to show 1
		cross_foot += (first_dig_product + last_dig_product)

		remnant = remnant // 10 # integer div to reduce to 6124 
		middle_digits = remnant % 10 # last dig now 4
		cross_foot += middle_digits # adds 4 to running total
		remnant = remnant // 10 # now remnant is 612  
		print(cross_foot)
	#return cross_foot

	return(10-cross_foot%10)%10

x = check_digit(7000)
print(x)