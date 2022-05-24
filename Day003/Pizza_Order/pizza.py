# Python Pizza Deliveries
# Author: Powell A. Mims
# This program calculates the cost of a pizza

print("\nWelcome to Python Pizza Deliveries!\n");

size = input("What size pizza would you like (S, M, L)? ");
if size == "S":
    cost = 15;
elif size == "M":
    cost = 20;
elif size == "L":
    cost = 25;
else:
    print("Did not enter a valid size (S, M, L).\nExiting program...");
    exit();

pepperoni = input("Add pepperoni (Y, N)? ");
if pepperoni == "Y":
    if size == "S":
        cost += 2;
    else:
        cost += 3;
elif pepperoni != "N":
    print("Did not enter valid pepperoni option (Y, N).\nExiting program...");
    exit();

cheese = input("Add extra cheese (Y, N)? ");
if cheese == "Y":
        cost += 1;
elif cheese != "N":
    print("Did not enter valid cheese option (Y, N).\nExiting program...");
    exit();

print(f"Total cost of your order is ${cost}");
