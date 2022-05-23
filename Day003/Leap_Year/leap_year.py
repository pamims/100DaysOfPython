# Leap Year
# Author: Powell A. Mims
# This program calculates whether a year is a leap year or not

print("\nWelcome to the Leap Year calculator!\n");

# Get input
year = int(input("Enter a year to check: "));

# Determine if it is a leap year
if year % 400 == 0:
    is_leap_year = True;
elif year % 100 == 0:
    is_leap_year = False;
elif year % 4 == 0:
    is_leap_year = True;
else:
    is_leap_year = False;

# Set the output string
if is_leap_year:
    message = "is";
else:
    message = "is not";

# Output
print(f"The year {year} {message} a leap year.\n");
