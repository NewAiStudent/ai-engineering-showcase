# AI Engineering Showcase

This repository contains various AI and programming projects.

## Command-Line Calculator

A simple command-line calculator written in Python that performs basic arithmetic operations.

### Features

- **Basic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **User-Friendly Interface**: Clear menu-driven interface
- **Input Validation**: Handles invalid input gracefully
- **Error Handling**: Prevents division by zero and other errors
- **Interactive**: Allows multiple calculations in one session

### How to Use

1. **Run the calculator**:
   ```bash
   python calculator.py
   ```

2. **Select an operation**:
   - Choose from options 1-5 (1=Addition, 2=Subtraction, 3=Multiplication, 4=Division, 5=Exit)

3. **Enter two numbers**:
   - The calculator will prompt you for two numbers
   - Supports both integers and decimals

4. **View the result**:
   - The calculation and result will be displayed

5. **Continue or exit**:
   - Choose whether to perform another calculation or exit

### Example Usage

```
========================================
Welcome to the Command-Line Calculator!
========================================

Available operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit

Select an operation (1-5): 1

You selected: +
Enter first number: 10
Enter second number: 5

Result: 10.0 + 5.0 = 15.0

Would you like to perform another calculation? (y/n): n

Thank you for using the calculator!
```

### Error Handling

The calculator handles various error conditions:

- **Invalid operation selection**: Prompts user to select a valid option
- **Invalid number input**: Asks for a valid number
- **Division by zero**: Shows an error message
- **General errors**: Displays appropriate error messages

### Requirements

- Python 3.x
- No additional dependencies required
