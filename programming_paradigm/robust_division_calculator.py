def safe_divide(numerator, denominator) -> float:
    try:
        numerator = float(numerator)
        denominator = float(denominator)

        division = numerator / denominator
        return division
    
    except ZeroDivisionError:
        return "can't divide by zero"
    except ValueError:
        return "Error: Error: Invalid input. Please enter numeric values for both numerator and denominator."

if __name__ == "__main__":
    safe_divide() 