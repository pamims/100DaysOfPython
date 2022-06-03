# Calculator
# Author: Powell A. Mims
# A simple calculator program :)

from calc_operations import operations
from ascii_imgs import calc_art

def is_number(value):
    try:
        float(value);
        return True;
    except ValueError:
        return False;
        
def get_operation():
    operation = "";
    while operation not in operations:
        print("These are the available operations: +, -, *, /");
        operation = input("Select an operation: ");
    return operation;

def get_operand():
    operand = "";
    while not is_number(operand):
        operand = input("Enter a valid number: ");
    return float(operand);

def check_if_finished():
    yes_no = { "y" : False, "n" : True };
    do_again = "";
    while do_again not in yes_no:
        do_again = input("Perform another calculation (Y, n)? ").lower();
    return yes_no[do_again];


# Start
print(calc_art);
print("\nWelcome to the Calculator!\n");

# Program loop
is_finished = False;
while not is_finished:
    # Get input
    operand1 = get_operand();
    operation = get_operation();
    operand2 = get_operand();

    # Find result
    function = operations[operation];
    result = function(operand1, operand2);
    print(f"Result: {result}");

    # Check if complete
    is_finished = check_if_finished();
    
# Complete
print("\nThank you for using the Calculator!\nGoodbye.\n");
