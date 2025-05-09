from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
   first_column()
   second_column()
   third_column()
   fourth_column()


# build columns 
def build_column():
    put_beeper()
    for i in range(4):
        while front_is_clear():
            move()
            put_beeper()

# first column
def first_column():
    turn_left()
    build_column()
    turn_right()
    move_four()

# second column
def second_column():
    turn_right()
    build_column()
    turn_left()
    move_four()

# third column
def third_column():
    turn_left()
    build_column()
    turn_right()
    move_four()

# fourth column
def fourth_column():
    turn_right()
    build_column()
    turn_left()

# turn_left three times
def turn_right():
    for i in range(3):
        turn_left()


# move function
def move_four():
    move()
    move()
    move()
    move()

if __name__ == '__main__':
    main()