# Tip Calculator
# Author: Powell A. Mims
# This program calculates how much each person should pay for a shared order

num_people = input("How many people are splitting the bill?\n    ");
cost = input("What is the order cost?\n    ");
tip_percent = input("What percent tip should be added?\n    ");

num_people = int(num_people);
tip_percent = float(tip_percent) / 100;
cost = float(cost)
cost_per_person = cost * (1 + tip_percent) / num_people;

print(f"Each person should pay ${cost_per_person}.");
