from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    Put beepers row by row, while one row is filled, reset to the start of the line and move to the next line then repeat putting beepers until it arrives to the last line beside the wall
    Fill Karel
    """
    while left_is_clear():
          fill_the_row()
          reset_to_next_row()
    fill_the_row()
    
def fill_the_row():
    put_beeper()
    while front_is_clear():
          move()
          put_beeper()
          
def reset_to_next_row():
    turn_around()
    while front_is_clear():
          move()
    turn_right()
    move()
    turn_right()
    
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()