from karel.stanfordkarel import *

# the start of the program
def main():
   while front_is_clear(): 
      invert_beeper()
      move()
   # to prevent a fencepost bug 
   invert_beeper()

# picks up a beeper if one is present 
# puts down a beeper otherwise 
def invert_beeper():
   # an if/else statement 
   if beepers_present():
      pick_beeper()
   else:
      put_beeper()