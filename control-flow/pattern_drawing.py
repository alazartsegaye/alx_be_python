# Prompt User for Pattern Size
pattern_size = int(input("Enter the size of the pattern: "))

# set row counter for the while loop
row = 0

# Use a while loop to repeat through rows
while pattern_size > row:
     # Use a for loop to print asterisks in each row
    for col in range(pattern_size): 
        print("*", end="") 
    print()
    row += 1