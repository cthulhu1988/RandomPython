# OLA106 BY Isaac Callison,  CSCI 1170-007, Due: 09/29/2016
# PROGRAM ID:  clearpapers.py / Pick up papers along perimeter of house 
# AUTHOR:  Isaac Callison
# INSTALLATION:  MTSU                                         
# REMARKS: Reeborg has been ill and unable to pick up the papers
# around his home. He should pick up each of these beepers and
# return all but one beeper to the vestibule of his home. The last
# beeper he will take back to bed.


def main():
    leave_home()
    #circle_perimeter()
    #deposit_beepers()
    #return_to_bed()
    turn_off()

#leave his house and pick up all the newspapers (beepers) 
def leave_home():
    find_wall()
    find_exit()

    #find wall
def find_wall():
    while front_is_clear():
        for x in range(3):
            if front_is_clear():
                turn_right()

        
    #find exit
def find_exit():
    turn_right()
    if not left_is_clear():
        if front_is_clear():
            move()
        else:
            turn_right()
            move()
    else:
        turn_left()
        move()
                #run along wall
        #find opening
        #stop in vestibule
        #exit
        
# perimeter of his property. 
#def circle_perimeter():
    #circle perimeter
    #pick up beepers
    # return to door
    
# Reeborg should then deposit all but one of these beepers 
# in vestibule of his house 
#def deposit_beepers():
    #return to door
    # enter door
        #stop in vestibule
    # drop beepers
        #drop all beepers
    # pick up on beeper
        # pick up on beeper
        
#return to bed with one beeper.

#def return_to_bed():
    
    # find wall again
    # find southwest corner
    #face west
    #turn off

# Pivot Reeborg 90 degrees to right.
def turn_right():
    for x in range(3):
        turn_left()


main()