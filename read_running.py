def main():
	my_file = open("video.txt", "r")

	total_vids = 0

	total_time = 0.0

	for line in my_file:
		total_vids += 1
		run_time = float(line)
		print("Video # " + str(total_vids) + " has a time of " + str(run_time) )
		total_time += float(run_time)
	
	my_file.close()

	print("The total running time is", total_time)




main()