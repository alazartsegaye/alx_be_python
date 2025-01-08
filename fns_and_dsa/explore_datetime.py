from datetime import datetime, timedelta

def display_current_datetime():
    # Get and format the current date and time
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

    # Prompt the user to enter a number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    # Call the function to calculate the future date
    calculate_future_date(current_date, days_to_add)

def calculate_future_date(current_date, days_to_add):
    # Calculate the future date
    future_date = current_date + timedelta(days=days_to_add)
    # Print the future date in a readable format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Main function
if __name__ == "__main__":
    display_current_datetime()
