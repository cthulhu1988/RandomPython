

def main():
	count = 0
	number_scores = 0
	list = []

	enter_scores = input("Enter a score: ")

	while enter_scores != '':
		list.append(enter_scores)
		enter_scores = input("Enter a score: ")

	list.sort()
	sorted_descending = []
	sorted_ascending = []
	sorted_ascending += list
	list.reverse()

	sorted_descending += list


	for ch in list:
		ch = float(ch)
		count += ch
		number_scores += 1
	if number_scores == 0:
		print("All scores stored:  []")
		print("No scores entered")
	else:
		average = count/number_scores
		average = format(average,".2f")
		print()
		print("All scores stored:",list)
		print("There are {} scores entered".format(number_scores))
		print ("The average is",average)
		print()
		print("After sorting in ascending order: ",sorted_ascending)
		print()
		print("rank: score")
		rank = 0
		for num in range(len(sorted_descending)):
			score = sorted_descending[rank]
			rank+=1
			print(rank,"  :   ",score)


main()