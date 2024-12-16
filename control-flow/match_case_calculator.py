# Prompt the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for the operation type
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using match-case
match operation:
    case "+":
        addition = num1 + num2
        print(f"The result is {addition}.")
    case "-":
        subtraction = num1 - num2
        print(f"The result is {subtraction}.")
    case "*":
        product = num1 * num2
        print(f"The result is {product}.")
    case "/": 
        if num2 == 0:
           print(f"Error: Cannot divide by zero.")
        else:
            division = num1 / num2
            print(f"The result is {division}.")
    case _:
        print("Invalid operation. Please choose +, -, *, or /.")

