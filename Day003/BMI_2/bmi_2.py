# BMI Calculator
# Author: Powell A. Mims
# This program calculates your BMI with English Units and
# tells you what your weight status is based on BMI

METERS_PER_FOOT = 0.3048;
KG_PER_POUND = 0.453952;

height = int(input("What is your height in feet?   "));
weight = int(input("What is your weight in pounds? "));

height *= METERS_PER_FOOT;
weight *= KG_PER_POUND;

bmi = weight / height ** 2;
bmi = round(bmi, 2);

if bmi < 18.5:
    status = "underweight";
elif bmi < 25:
    status = "normal weight";
elif bmi < 30:
    status = "overweight";
elif bmi < 35:
    status = "obese";
else:
    status = "clinically obese";

print(f"Your BMI is {bmi}.");
print(f"This bmi indicates that you are {status}.");
