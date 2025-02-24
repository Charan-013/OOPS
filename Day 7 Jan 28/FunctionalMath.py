from functools import reduce
import math
import random

def main():
    # Lambda Expressions
    add = lambda x, y: x + y
    print("Addition:", add(5, 3))

    # Functional Programming with List Comprehensions and Filters
    numbers = [1, 2, 3, 4, 5, 6]
    filtered = list(filter(lambda x: x % 2 == 0, numbers))
    print("Filtered Even Numbers:", filtered)

    # Using map with Math functions
    squares = list(map(math.sqrt, numbers))
    print("Square Roots:", squares)

    # Higher-Order Functions
    print("Custom Operation (Multiplication):",
          apply_operation(6, 7, lambda a, b: a * b))

    # Recursion
    print("Factorial of 5:", factorial(5))

    # Lazy Evaluation with Generators
    random_numbers = (random.random() for _ in range(5))
    print("Random Numbers:")
    for num in random_numbers:
        print(num)

def apply_operation(x, y, operation):
    return operation(x, y)

def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    main()
