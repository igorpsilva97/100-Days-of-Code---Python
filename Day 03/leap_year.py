print("Leap year check")
# Get the year from the user and convert it to an integer.
year = int(input("Which year do you want to check? "))

# --- Start of the leap year logic ---

# Rule 1: The year must be evenly divisible by 4.
if year % 4 == 0:

    # Rule 2 (Exception): If the year is also divisible by 100...
    if year % 100 == 0:

        # Rule 3 (Exception to the exception):
        # ...it must ALSO be divisible by 400 to be a leap year.
        if year % 400 == 0:
            print("Leap year")  # e.g., 2000. Divisible by 4, 100, and 400.
        else:
            print("Not Leap year.")  # e.g., 1900. Divisible by 4 and 100, but NOT 400.

    # This 'else' pairs with 'if year % 100 == 0'.
    else:
        print("Leap year.")  # e.g., 2024. Divisible by 4, but NOT by 100.

# This 'else' pairs with the first 'if year % 4 == 0'.
else:
    print("Not leap year.")  # e.g., 2021. Not divisible by 4.