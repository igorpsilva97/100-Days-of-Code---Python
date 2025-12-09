# Display a welcome message.
print("Welcome to the tip calculator!")

# Get the total bill amount from the user and convert it to a float.
bill = float(input("What was the total bill? $"))

# Get the tip percentage (as a whole number) from the user.
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Get the number of people splitting the bill.
people = int(input("How many people to split the bill? "))

# Convert the percentage (e.g., 15) to a decimal (e.g., 0.15).
tip_as_percent = tip / 100

# Calculate the total monetary amount of the tip.
total_tip_amount = bill * tip_as_percent

# Calculate the full bill (original bill + tip amount).
total_bill = bill + total_tip_amount

# Calculate how much each person must pay.
bill_per_person = total_bill / people

# Round the result to 2 decimal places.
final_amount = round(bill_per_person, 2)

# Display the final, rounded amount.
print(f"Each person should pay: ${final_amount}")