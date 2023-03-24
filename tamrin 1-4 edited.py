print("Welcome to the BMI calculator")
print("Please choose your preferred measurement system")
print("a : Imperial system")
print("b : Metric system")
op = input()


if op == "a":
    x = float(input("Please enter your weight in pounds: "))
    y = float(input("Please enter your height in feet: "))
    z = float(input("Please enter your height in inches: "))
    resulta = ((x * 0.45359237) / ((((y * 12) + z) * 0.0254)**2))
else:
    x = float(input("Please enter your weight in kilograms: "))
    y = float(input("Please enter your height in centimeters: "))
    resultb = x / ((y / 100)**2)

if op == "a":
    bmi = resulta
else:
    bmi = resultb

if bmi < 18.5:
    result = "You are underweight!"
elif 18.5 <= bmi <= 24.9:
    result = "You have a normal weight!"
elif 25 <= bmi <= 29.9:
    result = "You are overweight!"
elif 30 <= bmi <= 34.9:
    result = "You are obese!"
elif 35 <= bmi <= 39.9:
    result = "You are extremely obese!"
else:
    result = "Your BMI is above 39.9. Please consult a healthcare professional."

print(result)