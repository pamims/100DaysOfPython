# Treasure Map
# Author: Powell A. Mims
# This program takes a 2-digit coordinate to place an x on the map

row1 = [" ", " ", " "];
row2 = [" ", " ", " "];
row3 = [" ", " ", " "];
treasure_map = [row1, row2, row3];

print(f"{row1}\n{row2}\n{row3}\n");

print("Where do you want to put the treasure?");
coord = input("Enter coordinates as a 2-digit number (e.g., 23): ");

coord = [int(coord[0]) - 1, int(coord[1]) - 1];

treasure_map[coord[1]][coord[0]] = "X";

print(f"{row1}\n{row2}\n{row3}\n");
