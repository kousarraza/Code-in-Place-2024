# This tells python who Karel is!
from karel.stanfordkarel import *

# this program executes in a special function called main
def main():
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()
    move()
    put_beeper()
    move()

# the definition of turn_right
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# This is "boilerplate" code which launches your code
# when you hit the run button
if __name__ == '__main__':
    main()
