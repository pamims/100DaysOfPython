# Odd or Even
# Author: Powell A. Mims
# This program takes an input number and tells you whether it's odd or even

print("\nWelcome to Odd or Even!\n");
num = int(input("Enter an integer to check: "));

if num % 2 == 0:
    message = "even";
else:
    message = "odd";

print(f"The number {num} is {message}!\n");
