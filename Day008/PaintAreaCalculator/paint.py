# Paint Area Calculator
# Author: Powell A. Mims
# This program calculates how many cans of paint you will need to paint a wall

from math import ceil

PAINT_AREA = 53.8196 # square feet (5 square meters)

def paint_calc(height = 9, width = 10, coverage = PAINT_AREA):
    area = width * height;
    num_cans = ceil(area / coverage);
    return num_cans;

def is_num(input = ""):
    try:
        float(input);
        return True;
    except ValueError:
        return False;

print("\nWelcome to the Paint Area Calculator!\n");
width = input("what is the width of the wall (ft)? ");
height = input("what is the height of the wall (ft)? ");

if is_num(width) == False or is_num(height) == False:
    print("This program only works if you input numbers.");
    exit();

width = float(width);
height = float(height);

num_cans = paint_calc(height, width);

print(f"It will take {num_cans} cans of paint to paint this wall.\n");
