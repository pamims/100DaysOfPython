# Calculator
# Author: Powell A. Mims
# A simple calculator program :)

from ascii_imgs import calc_art
from input_functions import get_operand, get_operation_function, check_if_finished

# Start
print(calc_art);
print("\nWelcome to the Calculator!\n");

# Program loop
is_finished = False;
while not is_finished:
    # Get input
    operand1 = get_operand();
    operation_function = get_operation_function();
    operand2 = get_operand();

    # Find result
    result = operation_function(operand1, operand2);
    print(f"Result: {result}");

    # Check if complete
    print("");
    is_finished = check_if_finished();
    
# Complete
print("\nThank you for using the Calculator!\nGoodbye.\n");
