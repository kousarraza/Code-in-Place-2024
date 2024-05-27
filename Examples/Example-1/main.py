
from karel.stanfordkarel import *

def main():
   
  move()
  turn_right()
  put_beeper()
  turn_left()
  move()
def turn_right():
  turn_left()
  turn_left()
  turn_left()
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()