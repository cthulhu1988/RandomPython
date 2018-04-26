# cla12(a) BY Isaac Callison, CSCI 1170-007, Due: 11/8/2016, Lab Assitant: Arthur
# PROGRAM ID: ch15p7.py / parse golf data
# AUTHOR: Isaac Callison
# INSTALLATION:  MTSU
# Remarks: parses data into a list of scores and players
# determines the winner  

def main():
    file = open("golf.txt", "r")
    players = []
    number = 0
    scores = []
    line = file.readline()

    while line != '':
    	players.append(line.strip())
    	number +=1
    	line = file.readline()
    	scores.append(int(line))
    	line = file.readline()

    lowScore, lowestIndex = find_lowest(scores)
    lowest_player = players[lowestIndex]
    	
    print("There are {} players in file golf.txt".format(number))
    print()
    print("Players             scores")
    for i in range(len(scores)):
    	print(format(players[i],'<23s'),(scores[i]))
    	

    print()
    print("The winner is {} with the score of {}".format(lowest_player,lowScore))	

def find_lowest(lst):
    list2 = [x for x in lst]
    x = (min(list2))
    return(x,(list2.index(x)))

main()
