print("BMI calculator")

# Set the weight in kilograms.
weight = 85
# Set the height in meters.
height = 1.85

# Calculate BMI using the formula: weight / (height * height).
bmi = weight / (height ** 2)

# Print the calculated BMI, formatted to 2 decimal places.
print(f"Your BMI is: {bmi:.2f}")

# Check if BMI is less than 18.5.
if bmi < 18.5:
    print("underweight")
# If it got here, BMI is >= 18.5. We only need to check the upper limit.
elif bmi < 25:
    print("normal weight")
# If it got here, BMI is >= 25.
elif bmi < 30:
    print("overweight")
# If it got here, BMI is >= 30.
else:
    print("obese")