# Ask for height and weight
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate BMI
bmi= weight/(height**2)

print(f"Your BMI is {bmi:.2f}")