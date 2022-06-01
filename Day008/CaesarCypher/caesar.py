# Caeser Cypher
# Author: Powell A. Mims
# This program encodes and decodes caesar cypher encrypted messages.

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"];

def encode(message = "", skip = 0):
    output = "";
    for letter in message:
        if letter.isalpha():
            is_upper = letter.isupper();
            if is_upper:
                letter = letter.lower();
            index = ALPHABET.index(letter);
            index += skip;
            index %= 26;
            letter = ALPHABET[index];
            if is_upper:
                letter = letter.upper();
        output += letter;
    return output;

def decode(message = "", skip = 0):
    skip *= -1;
    return encode(message, skip);


print("\nWelcome to the Caesar Cypher program!\n");

message = input("Enter the message: ");

direction = input("Type 'encode' or 'decode' to select what you would like to do with your message: ");
if direction not in ["encode", "decode"]:
    print("Invalid instruction.");
    exit();

try:
    skip = int(input("What is the offset for the message? "));
except ValueError:
    print("Argument must be an integer.");
    exit();

if direction == "encode":
    message = encode(message, skip);
else:
    message = decode(message, skip);

print(f"Output: {message}\n");
