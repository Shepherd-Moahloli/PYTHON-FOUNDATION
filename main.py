"""
Main Python application entry point.
"""

def main():
    """Main function to demonstrate a simple Python application."""
    print("Hello, World!")
    print("Welcome to your new Python project!")
    
    # Example of basic Python functionality
    numbers = [1, 2, 3, 4, 5]
    squared = [x**2 for x in numbers]
    
    print(f"Original numbers: {numbers}")
    print(f"Squared numbers: {squared}")
    
    # Example function call
    result = calculate_sum(numbers)
    print(f"Sum of numbers: {result}")


def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)


if __name__ == "__main__":
    main()
