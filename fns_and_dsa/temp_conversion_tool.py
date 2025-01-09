# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5   # Conversion factor from Celsius to Fahrenheit

def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius.
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius  # Return the converted temperature

def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit.
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit  # Return the converted temperature

def main():
    try:
        # Get user input
        temperature = float(input("Enter the temperature to convert: "))  # Prompt for temperature
        celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()  # Prompt for unit

        # Perform conversion based on user input
        if celsius_or_fahrenheit == "c":
            fahrenheit = convert_to_fahrenheit(temperature)  # Call the function with the temperature
            print(f"{temperature}°C is {fahrenheit:.2f}°F")  # Display the converted temperature
        elif celsius_or_fahrenheit == "f":
            celsius = convert_to_celsius(temperature)  # Call the function with the temperature
            print(f"{temperature}°F is {celsius:.2f}°C")  # Display the converted temperature
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")  # Handle invalid unit input
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")  # Handle non-numeric input

if __name__ == "__main__":
    main()  # Run the main function
