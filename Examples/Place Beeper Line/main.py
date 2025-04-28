from karel.stanfordkarel import *

def main():
    while front_is_clear():
        put_beeper() 
        move()
    put_beeper()
# don't change this code
if __name__ == '__main__':
    main()