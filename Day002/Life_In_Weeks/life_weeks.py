# Life In Weeks
# Author: Powell A. Mims
# This program calculates how much time you have left to live
# based on your expected maximum age.

age_in_years = float(input("How many years old are you? "));
max_age = float(input("How old do you think you'll live to? (90?) "));

years_left = max_age - age_in_years;
months_left = years_left * 12;
weeks_left = years_left * 52;
days_left = years_left * 365;

print(f"If you only live to be {max_age}, you have:");
print(f"\t{years_left} years to go");
print(f"\t{months_left} months to go");
print(f"\t{weeks_left} weeks to go");
print(f"\t{days_left} days to go");
