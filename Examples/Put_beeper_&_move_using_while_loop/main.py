# File: BeeperLine.py
# ------------------------------
# Uses a while loop to place a line of beepers.
# This program works for a world of any size.
from karel.stanfordkarel import *

# program starts at main
def main():
   # repeats until karel faces a wall
   while front_is_clear():
      # place a beeper on current square
      put_beeper()
      # move to the next square
      move()
   # solves the fencepost bug
   put_beeper()