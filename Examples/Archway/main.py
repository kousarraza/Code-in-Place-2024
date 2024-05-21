
from karel.stanfordkarel import *

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    turn_left()
    move_three_times()
    turn_right()
    move_three_times()
    turn_right()
    move_three_times()
    turn_left()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def move_three_times():
    move()
    move()
    move()
if __name__ == '__main__':
    main()