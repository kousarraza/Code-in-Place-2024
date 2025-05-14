from karel.stanfordkarel import *

def main():
    put_beeper()
    # make Karel draw one row and jupm to next row, until reaching the last row at the top, using the condition 'left_is_clear()'.
    while left_is_clear():
        draw_row()
        junp_row() 
    #drawing the last row at the top
    draw_row()
    #Karel return to bottom laft corner
    return_to_starting_point()
    
def draw_row():
    
    while front_is_clear():
        #this is a if condition whithin a if condition, I use it here because in the 3x1 world, Karel would have no room to move foward, so Karel have to check if front is clear before every move
        if front_is_clear():
            #this makes Karel move two steps and drop a beeper
            move()
            if front_is_clear():
                move()
                put_beeper()    
        
def junp_row():
    #after finish drawing one row, Karel return to the starting point
    turn_around()
    while front_is_clear():
        move()
    #this if else condition tell if there is a beeper at the starting point
    if beepers_present():
        #if there is a beeper at the atarting point of the first row, Karel would junp to next row, move one step to the right and drop a beeper
        turn_right()
        move()
        turn_right()
        #Karel need to check before move forward, because in the 3x1 world, Karel would have no room to move foward
        if front_is_clear():
            move()
            put_beeper()
    else:
        #if there is no beeper at the atarting point of the first row, karel would jump to next row and put a beeper
        turn_right()
        move()
        turn_right()
        put_beeper()
    
#Karel return to bottom left corner of the map
def return_to_starting_point():
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()
    

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()