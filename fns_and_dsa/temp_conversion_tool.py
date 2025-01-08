FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius.
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius  # Return the converted temperature

def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit.
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit  # Return the converted temperature

# Get user input
temperature = float(input("Enter the temperature to convert: "))
celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

# Perform conversion based on user input
if celsius_or_fahrenheit == "c":
    fahrenheit = convert_to_fahrenheit(temperature)  # Call the function with the temperature
    print(f"{temperature}°C is {fahrenheit}°F")
elif celsius_or_fahrenheit == "f":
    celsius = convert_to_celsius(temperature)  # Call the function with the temperature
    print(f"{temperature}°F is {celsius}°C")
else:
    print("Enter a valid temperature and unit.")
