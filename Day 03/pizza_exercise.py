print("Welcome to Python Pizza Deliveries!")

# Get the desired pizza size from the user (S, M, or L).
size = input("What size pizza do you want? S, M, or L ")
# Ask the user if they want to add pepperoni (Y or N).
add_pepperoni = input("Do you want pepperoni? Y or N ")
# Ask the user if they want to add extra cheese (Y or N).
extra_cheese = input("Do you want extra cheese? Y or N ")

# Initialize the total bill to 0 before calculating.
bill = 0

# --- 1. Calculate base price based on size ---
if size == "S":
  bill += 15  # Small Pizza base price: $15
elif size == "M":
  bill += 20  # Medium Pizza base price: $20
else:
  bill += 25  # Large Pizza base price: $25 (assumes L)

# --- 2. Add cost for pepperoni (if requested) ---
if add_pepperoni == "Y":
  # Pepperoni price depends on the pizza size.
  if size == "S":
    bill += 2  # Pepperoni for Small: +$2
  else:
    bill += 3  # Pepperoni for Medium or Large: +$3

# --- 3. Add cost for extra cheese (if requested) ---
if extra_cheese == "Y":
  bill += 1  # Extra cheese for any size: +$1

# --- 4. Display the final total ---
# Print the final calculated bill using an f-string.
print(f"Your final bill is ${bill}")