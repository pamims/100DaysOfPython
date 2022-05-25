# Banker Roulette
# Author: Powell A. Mims
# This program takes a list of names, separated by a comma and a space,
# and selects a name randomly (to pay the bill)

import random

print("\nWelcome to Banker Roulette\n");
names = input("Provide a list of names separated by commas and spaces: ");
names = names.split(", ");
selection = random.choice(names);
print(f"\n{selection} should pay the bill.");
