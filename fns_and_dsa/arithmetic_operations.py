# arithmetic_operations.py

def perform_operation(num1, num2, operation):

    """
    Perform an arithmetic operation on two numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float or str: The result of the operation or an error message if the operation is invalid.
    """
    if operation == "add":
        return num1+num2
    elif operation == "subtract":
        return num1-num2
    elif operation == "multiply":
        return num1*num2
    elif operation == "divide":
        if num2 != 0:
            return num1/num2
        return "Error: number can't be divided by 0"
    else:
        return "Error: enter a valid operation!"

