def main():
    move_to_the_beeper()
    pick_beeper()
    face_south()
    turn_off()

# Traverse systematically until stopping on beeper corner
def move_to_the_beeper():
    go_to_northwest_corner()
    face_south()
    while not on_beeper():
        move_to_next_adjacent_street_corner()

# Go to room's northwest street corner
def go_to_northwest_corner():
    face_north()
    move_to_wall()
    orient_Nw()
    
    
# Advance forward to a wall
def move_to_wall():
    while front_is_clear():
        move()
    
# Move to next adjacent street corner
def move_to_next_adjacent_street_corner():
        while front_is_clear():
            move()
        if not front_is_clear():
            move_one_avenue_east()

# Move east to adjacent avenue corner
def move_one_avenue_east():
    if facing_north():
        if right_is_clear():
            turn_right()
            move()
            turn_right()
    else:
        if facing_south():
            if left_is_clear():
                turn_left()
                move()
                turn_left()
# Face Reeborg north
def face_north():
    while not facing_north():
        turn_left()
            
# Face Reeborg south
def face_south():
    while not facing_south():
        turn_left()
    
# Pivot 90 degrees to the right
def turn_right(): 
    for x in range(3):
        turn_left() 
#
def orient_Nw():
    if left_is_clear():
        turn_left()
        while front_is_clear():
            move()
   

# Call the main function.
main()
