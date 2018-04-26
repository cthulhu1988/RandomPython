# OLA106 BY Isaac Callison,  CSCI 1170-007, Due: 010/6/2016
# PROGRAM ID:  classrooms.py / Output formatted room triplet data. 
# AUTHOR:  Isaac Callison
# INSTALLATION:  MTSU
# REMARKS: Program reads and processes input data, displays properly
# formatted output data, and exits when a sentinal value is detected. 
import sys

def main():
    # set accumulators needed for program to execute correctly:
    total_capacity = 0
    count = 0
    total_enrollment = 0
    free_rooms = 0

    # Priming read: room,capacity,size integer triplets from standard input
    room,capacity,size = map(int,sys.stdin.readline().split())
    # Print header
    print("Room  Capacity  Size  Empty Seats  Status")
    
    # Process triplets until EOF-sentinel encountered
    while room>=0:
        #calculate empty seats for each iteration.       
        empty_seats = (capacity - size)
        # Logic to check for room status. 
        if(empty_seats > 0):
            status = "OPEN"
            free_rooms += 1
        else:
            status = "FULL"

        print(format(room,"4d"), format(capacity,">9d"), format(size,">5d"), format(empty_seats,"7d"), format(status,">11s"))
        # Increment accumulators
        count += 1
        total_capacity+=capacity
        total_enrollment += size
        # Recurring read: room,capacity,size
        room,capacity,size = map(int,sys.stdin.readline().split())
    # Print Stars
    for n in range(41):
        print("*", end="")
    print() 
    print("Rooms: ",count)
    print("Overall Capacity:",(total_capacity))
    print("Total Enrollment:",total_enrollment)
    print("Number of Open Rooms Remaining:",free_rooms)

    for n in range(41):
        print("*", end="")
    print()

main()

