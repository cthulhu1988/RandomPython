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
    circle_perimeter()
    deposit_beepers()
    return_to_bed()
    turn_off()

#leave his house and pick up all the newspapers (beepers)
# define logic to exit house in leave_home
def leave_home():
    find_wall()
    find_exit()
    exit_vestibule()
    
# Start by finding wall
def find_wall():
    while front_is_clear():
        for x in range(4):
            if front_is_clear():
                turn_right()
                
# locate exit and set up for exit from vestibule
def find_exit():
    turn_right()
    if front_is_clear():
        move()
    while not left_is_clear():
        if not left_is_clear():
            if front_is_clear():
                move()
            else:
                turn_right()
                move()
    if left_is_clear():
        if right_is_clear():
            turn_left()
            move()
    if not left_is_clear():
        if not right_is_clear():
            pass

# logic to exit vestibule after running find_exit logic
# checks for beeper intially, orients for circle_perimeter logic
# and checks for beepers along the way.
def exit_vestibule():
    while on_beeper():
        pick_beeper()
    if front_is_clear():
        if left_is_clear():
            turn_left()
        move()
    while on_beeper():
        pick_beeper()
    if left_is_clear():
        turn_left()
        move()
    while on_beeper():
        pick_beeper()

#circle perimeter of his property
#pick up all beepers along perimeter, return to entrance 
def circle_perimeter():
    while on_beeper():
        pick_beeper()
    while not on_beeper():
        if not left_is_clear():
            if front_is_clear():
                move()
                while on_beeper():
                    pick_beeper()
        if not front_is_clear():
            if not left_is_clear():
                turn_right()
                while on_beeper():
                    pick_beeper()
        if front_is_clear():
            if left_is_clear():
                turn_left()
                move()
                while on_beeper():
                    pick_beeper()
        if left_is_clear():
            if not front_is_clear():
                turn_left()
                move()
        while on_beeper():
            pick_beeper()

# Reeborg should then deposit all but one of these beepers 
# in vestibule of his house 
# Reeborg starts this logic stopped in vestibule with beepers
def deposit_beepers():
    while carrying_beepers():
        put_beeper()
    pick_beeper()
        
#return to bed with one beeper.
 # find wall again
    # find southwest corner if left_is_clear():if leftif left_is_clear():
    #face west
    #turn off
def return_to_bed():
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_left()
    
   

# Pivot Reeborg 90 degrees to right.
def turn_right():
    for x in range(3):
        turn_left()


main()