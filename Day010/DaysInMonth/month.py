# Days in Month
# Author: Powell A. Mims
# This program tells you how many days are in the month

def is_leap_year(year):
    if year % 400 == 0:
        return True;
    if year % 100 == 0:
        return False;
    if year % 4 == 0:
        return True;
    return False;

month_days = {
    "jan" : 31,
    "feb" : 28,
    "mar" : 31,
    "apr" : 30,
    "may" : 31,
    "jun" : 30,
    "jul" : 31,
    "aug" : 31,
    "sep" : 30,
    "oct" : 31,
    "nov" : 30,
    "dec" : 31
    };

print("\nWelcome to Days in Month program!\n");

print("What month would you like to check?");
month = input("Enter a 3-letter abbreviation (ex. 'Feb'): ");
month = month.lower();

if month not in month_days:
    print("You did not enter a valid month.");
    exit();

days = month_days[month];

if days == 28:
    year = input("What year is the month in? ");
    try:
        year = int(year);
    except ValueError:
        print("You did not enter a valid year.");
        exit();
    if is_leap_year(year):
        days = 29;

print(f"{month.title()} has {days} days in it.\n");
