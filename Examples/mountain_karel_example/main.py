from karel.stanfordkarel import *

# The mountain karel example from the video!

def main():
    climb_up_mountain()
    plant_flag()
    climb_down()
    
def climb_up_mountain():
    # post: karel is at the top of the mountain
    # facing east
    while front_is_blocked():
        step_up()
        
def step_up():
    # Karel takes one step up the mountain
    # pre: karel is facing the mountain
    # post: karel is facing the mountain one step up
    turn_left()
    move()
    turn_right()
    move()

def plant_flag():
    # a beeper, the national flag of karel land
    put_beeper()

def climb_down():
    # post: karel is at the bottom of the mountain
    # pre: kare is at the top, facing right
    while front_is_clear():
        step_down()
    
def step_down():
    # pre: karel is on a step, facing right (East)
    # post: karel is on the next step, facing right
    move()
    turn_right()
    move()
    turn_left()


def turn_right():
    # Makes karel turn in the clock-wise direction.
    # Works in any pre-condition state!
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()