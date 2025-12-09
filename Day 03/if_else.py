print("Welcome to the rollercoaster")

# Ask the user for their height and convert the input string to an integer.
height = int(input("What is your height in cm? "))

# Check if the user's height is greater than 120 cm.
if height > 120:
    # If the condition is True, print this message.
    print("You can ride the rollercoaster")
else:
    # If the condition (height > 120) is False, print this message.
    print("Sorry, you cannot ride the rollercoaster")