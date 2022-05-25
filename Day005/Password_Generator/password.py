# Password Generator
# Author: Powell A. Mims
# Creates a randomly generated password based on user input

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'];

print("\nWelcome to the Password Generator!\n");
num_letters = int(input("How many letters should be in the password? "));
num_numbers = int(input("How many numbers should be in the password? "));
num_symbols = int(input("How many symbols should be in the password? "));

parameters = [num_letters, num_numbers, num_symbols];
characters = [letters, numbers, symbols];

password_chars = [];

for p in parameters:
    if p > 0:
        for i in range(0, p):
            password_chars.append(random.choice(characters[0]));
    characters.pop(0);

random.shuffle(password_chars);

password = "";
for c in password_chars:
    password += c;

print(password);
