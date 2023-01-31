height=float(input("Please enter your height (in inches): "))
weight=float(input("Please enter your weight (in lbs): "))
bmi=round(float(weight * 703 / height ** 2), 2)

if bmi < 16.0:
    category = "Severely Underweight"
elif bmi < 18.4:
    category = "Underweight"
elif bmi < 24.9:
    category = "Normal"
elif bmi < 29.9:
    category = "Overweight"
elif bmi < 34.9:
    category = "Moderately Obese"
elif bmi < 39.9:
    category = "Severely Obese"
elif bmi > 39.9:
    category = "Morbidly Obese"

print(f'Your BMI of {bmi} makes you {category}')