from karel.stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.


def main():
    move_to_beeper()
    pick_beeper()
    return_to_start()

def move_to_beeper():
   move()
   move()
   turn_left()
   turn_left()
   turn_left()
   move()
   turn_left()
   move()


   

def return_to_start():
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
    move()
    turn_left()
    turn_left()
    
    
    
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()