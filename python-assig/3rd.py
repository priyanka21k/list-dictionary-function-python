"""
Write a program to calculate BMI of a person after
inputting the weight in kgs and height in meters
and then print the nutritional status as per the given table

"""

height = float(input("Your height in metres:"))
weight = int(input("Your weight in kilograms:"))
bmi = round(weight/ (height * height), 1)

if bmi <= 18.5:
     print('Your BMI is', bmi, 'which means your nutritional status is underweight.')

elif bmi > 18.5 and bmi < 25:
     print('Your BMI is', bmi, 'which means your nutritional status is normal.')

elif bmi > 25 and bmi < 30:
     print('Your BMI is', bmi, 'which means your nutritional status is overweight.')

elif bmi > 30:
     print('Your BMI is', bmi, 'which means your nutritional status is obese.')

else:
    print('There is an error with your input')
