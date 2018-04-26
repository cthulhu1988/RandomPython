# cla9b BY Isaac Callison, CSCI 1170-007, Due: 10/20/2016, Lab Assitant: Arthur
# PROGRAM ID: ch5x13.py / Falling Distance 
# AUTHOR: Isaac Callison
# INSTALLATION:  MTSU
# Remarks: Takes a numbers as an input then compute the amount of time
# an object has traveled on that interval.


def main():

        time_interval = int(input("Enter time in seconds that object has been falling: "))
        for x in range(1, time_interval+1):
                falling_time = falling_distance(x)
                print("second:",x,"distance travled:", format(falling_time,".2f"),"meters")

def falling_distance(time):
        distance = (1/2)*9.8 * time ** 2
        return distance
        
main()
