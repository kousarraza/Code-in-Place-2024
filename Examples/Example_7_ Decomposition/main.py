from karel.stanfordkarel import *
def main():
   move()
   fill_pothole()
   move()

# Fills the pothole beneath Karel's current position by 
# placing a beeper on that corner. For this function to work 
# correctly, Karel must be facing east immediately above the 
# pothole. When execution is complete, Karel will have 
# returned to the same square and will again be facing east.
def fill_pothole():
   turn_right()
   move()
   put_beeper()
   turn_around()
   move()
   turn_right()

# Turns Karel 90 degrees to the right. 
def turn_right():
   turn_left()
   turn_left()
   turn_left()

# Turns Karel around 180 degrees. 
def turn_around():
   turn_left()
   turn_left()