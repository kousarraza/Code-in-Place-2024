"""
Program: multiply two numbers
--------------------
This program asks the user for two
integers and prints the value of the first number
multiplied with the second
"""

def main():
    print("This program multiplies two numbers.")
    first_number=input("Enter first number:")
    second_number=input("Enter second number:")
    first_number=int(first_number)
    second_number=int(second_number)
    c=first_number*second_number
    print(c)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()