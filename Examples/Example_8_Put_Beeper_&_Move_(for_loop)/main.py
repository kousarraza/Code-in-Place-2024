# File: PlaceManyBeepers.py
# -----------------------------
# Places 42 beepers using a for loop
from karel.stanfordkarel import *

def main():
   move()
   # repeat put_beeper many times 
   for i in range(42):
  	  put_beeper()
   move()