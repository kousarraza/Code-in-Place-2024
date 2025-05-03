from karel.stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    move()
    move()
    fill_pothole()
    

def fill_pothole():
    pick_beeper()
    move()
    turn_left()
    move()
    move()
    put_beeper()
    turn_around()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_around()
    
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