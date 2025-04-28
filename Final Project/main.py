import math
from sympy import isprime, sqrt

def is_whole_number(n):
    return n == int(n)

def is_irrational_number(n):
    return not is_whole_number(n) and not (n == float(int(n)))

def is_natural_number(n):
    return n > 0 and is_whole_number(n)

def is_prime_number(n):
    return n > 1 and isprime(n)

def is_decimal(n):
    return isinstance(n, float) and not n.is_integer()

def is_perfect_square(n):
    return n == int(n) and int(sqrt(n))**2 == n

def find_factors(n):
    n = abs(int(n))
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def analyze_number(n):
    results = {
        "even": False,
        "odd": False,
        "whole": False,
        "irrational": False,
        "natural": False,
        "prime": False,
        "decimal": False,
        "perfect_square": False,
        "factors": []
    }

    if is_whole_number(n):
        results["whole"] = True
        if n % 2 == 0:
            results["even"] = True
        else:
            results["odd"] = True
        if is_natural_number(n):
            results["natural"] = True
        if is_prime_number(n):
            results["prime"] = True
        if is_perfect_square(n):
            results["perfect_square"] = True
        results["factors"] = find_factors(n)
    else:
        if is_irrational_number(n):
            results["irrational"] = True
        if is_decimal(n):
            results["decimal"] = True

    return results

def main():
    while True:
        user_input = input("Enter a number (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        try:
            # Try to convert to float
            number = float(user_input)
            
            # Analyze the number
            analysis = analyze_number(number)
            
            # Display results
            print(f"\nAnalysis of {number}:")
            for key, value in analysis.items():
                if key != "factors":
                    print(f"{key.capitalize()}: {value}")
                else:
                    print(f"{key.capitalize()}: {', '.join(map(str, value))}")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        # Ask if the user wants to continue
        continue_input = input("\nDo you want to analyze another number? (yes/no): ").lower()
        if continue_input != 'yes':
            break

if __name__ == "__main__":
    main()
