# Prime Number Checker
# Author: Powell A. Mims
# This program checks if a number is prime or not

def is_prime(num):
    if num == 4:            # 4 / 2 = 2 --> range(2, 2) is empty. Skips
        return False;       # for loop and causes erroneous true return.
    max = int(num / 2);
    for i in range(2, max):
        if num % i == 0:
            return False;
    return True;

print("\nWelcome to the Prime Number Checker!\n");
number = input("What number should we check? ");

if not number.isnumeric():
    print("This program only works on integers.");
    exit();

number = int(number);
if is_prime(number):
    message = "";
else:
    message = " not";

print(f"This number is{message} prime.\n");
