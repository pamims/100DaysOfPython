# Tip Calculator
# Author: Powell A. Mims
# This program calculates how much each person should pay for a shared order

print("Welcome to the Tip Calculator!\n");

num_people = input("How many people are splitting the bill? ");
cost = input("What is the order cost? $");
tip_percent = input("What percent tip should be added? (10, 12, 15?) ");

num_people = int(num_people);
tip_percent = float(tip_percent) / 100;
cost = float(cost)
cost_per_person = round(cost * (1 + tip_percent) / num_people, 2);

print(f"Each person should pay ${cost_per_person}.");
