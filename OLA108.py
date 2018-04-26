# OLA108 BY Isaac Callison,  CSCI 1170-007, Due: 010/18/2016
# PROGRAM ID:  treasure.py / Reeborg reads beeper-clues to locate
# treasure. 
# AUTHOR:  Isaac Callison
# INSTALLATION:  MTSU                                         
# REMARKS: Reeborg must navigate to a treasure through direction 
# beepers and beepers that indicate proper pace count. Upon landing
# on a trove of beepers with the sentinal value of '5' Reeborg
# will scoop up the beepers, face north, and shut off. 

def main():
    direction = 0
    while direction != 5:
        direction = which_direction()
        if direction != 5:
            find_pace_count()
            pace_cnt = pace_beepers()
            #double_back()
            orient_direction(direction)
            walking_plank(pace_cnt)
        else:
            while on_beeper():
                pick_beeper()
            while not facing_north():
                turn_left()
    turn_off()
    
def which_direction():
    compass = 0
    while on_beeper():
        pick_beeper()
        compass+=1
    for x in range(compass):
        put_beeper()
    return compass

def find_pace_count():
    while not front_is_clear():
        turn_left()
    if front_is_clear():
        move()
    while not on_beeper():
        double_back()
        turn_left()
        if not front_is_clear():
            turn_left()
        move()
# Determine number of beepers on corner
# Returns number of paces to move
def pace_beepers():
    pace_count = 0
    while on_beeper():
        pick_beeper()
        pace_count+=1
    for x in range(pace_count):
        put_beeper()
        double_back()
    return pace_count
    
# takes input from which_direction to orient Reeborg
def orient_direction(direction):
    if direction == 1:
        while not facing_east():
            turn_left()
    elif direction == 2:
        while not facing_north():
            turn_left()
    elif direction == 3:
        while not facing_west():
            turn_left()
    elif direction == 4:
        while not facing_south():
            turn_left()
    elif direction == 5:
        end == True
        return end

def walking_plank(paces):
    for x in range(paces):
        move()

def double_back():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()

main()
 