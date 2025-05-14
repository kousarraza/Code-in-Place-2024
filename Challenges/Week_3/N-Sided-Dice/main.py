import random


def roll_dice(num_sides):
    return random.randint(1, num_sides)

def main():
    num_sides = int(input("How many sides does your dice have? "))
    roll_result = roll_dice(num_sides)
    print("Your roll is", roll_result)

if __name__ == '__main__':
    main()