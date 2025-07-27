#!/usr/bin/env python3
"""
Command-line Calculator
A simple calculator that performs basic arithmetic operations.
"""

def get_operation():
    """Get the operation from user input."""
    while True:
        print("\nAvailable operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        choice = input("\nSelect an operation (1-5): ").strip()
        
        if choice == '1':
            return '+'
        elif choice == '2':
            return '-'
        elif choice == '3':
            return '*'
        elif choice == '4':
            return '/'
        elif choice == '5':
            return 'exit'
        else:
            print("Invalid choice. Please select 1-5.")

def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate(num1, num2, operation):
    """Perform the calculation based on the operation."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Error: Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation.")

def main():
    """Main calculator function."""
    print("=" * 40)
    print("Welcome to the Command-Line Calculator!")
    print("=" * 40)
    
    while True:
        # Get operation from user
        operation = get_operation()
        
        if operation == 'exit':
            print("\nThank you for using the calculator!")
            break
        
        # Get numbers from user
        print(f"\nYou selected: {operation}")
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        
        # Perform calculation
        try:
            result = calculate(num1, num2, operation)
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        except ValueError as e:
            print(f"\n{e}")
        except Exception as e:
            print(f"\nAn error occurred: {e}")
        
        # Ask if user wants to continue
        continue_calc = input("\nWould you like to perform another calculation? (y/n): ").strip().lower()
        if continue_calc not in ['y', 'yes']:
            print("\nThank you for using the calculator!")
            break

if __name__ == "__main__":
    main() 