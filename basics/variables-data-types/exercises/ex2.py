# Ask for the person's weight and height, calculate BMI and display the result.

weight = float(input("What is your weight? "))
height = float(input("What is your height in meters? "))

bmi = weight / height ** 2

print("Your BMI is: ", bmi)