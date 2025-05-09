# File: BeeperCollectingKarel.py
# --------------------------------
# The BeeperCollectingKarel class collects all the beepers
# in a series of vertical towers and deposits them at the
# eastmost corner on 1st row.
from karel.stanfordkarel import *

def main():
   collect_all_beepers()
   drop_all_beepers()
   return_home()

# Collects the beepers from every tower by moving along 1st
# row, calling collect_one_tower at every corner.  The
# postcondition for this function is that Karel is in the
# easternmost corner of 1st row facing east.
def collect_all_beepers():
   while front_is_clear():
      collect_one_tower()
      move()
   collect_one_tower()

# Collects the beepers in a single tower. When collect_one_tower
# is called, Karel must be on 1st row facing east.  The
# postcondition for collect_one_tower is that Karel must again
# be facing east on that same corner.
def collect_one_tower():
   turn_left()
   collect_line_of_beepers()
   turn_around()
   move_to_wall()
   turn_left()

# Collects a consecutive line of beepers. The end of the beeper
# line is indicated by a corner that contains no beepers.
def collect_line_of_beepers():
   while beepers_present():
      pick_beeper()
      if front_is_clear():
         move()

# Drops all the beepers on the current corner.
def drop_all_beepers() :
   while beepers_in_bag():
      put_beeper()

# Returns Karel to its initial position at the corner of 1st
# Avenue and 1st row, facing east.  The precondition for this
# function is that Karel must be facing east somewhere on 1st
# row, which is true at the conclusion of collect_all_beepers.
def return_home():
   turn_around()
   move_to_wall()
   turn_around()

# Moves Karel forward until it is blocked by a wall.
def move_to_wall():
   while front_is_clear():
      move()

# Turns Karel 180 degrees around
def turn_around():
   turn_left()
   turn_left()