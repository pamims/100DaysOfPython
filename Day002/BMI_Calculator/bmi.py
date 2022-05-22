# BMI Calculator
# Author: Powell A. Mims
# This program calculates your BMI with English Units

METERS_PER_FOOT = 0.3048;
KG_PER_POUND = 0.453952;

height = int(input("What is your height in feet?   "));
weight = int(input("What is your weight in pounds? "));

height *= METERS_PER_FOOT;
weight *= KG_PER_POUND;

bmi = weight / height ** 2;

print(f"Your BMI is {bmi}");
