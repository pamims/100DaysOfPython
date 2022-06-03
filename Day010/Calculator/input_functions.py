from calc_operations import operations

def is_number(value):
    """Determine if the string input can convert to a float"""
    try:
        float(value);
        return True;
    except ValueError:
        return False;
        
def get_operation_function():
    """Get input for selecting an operation"""
    operation = "";
    while operation not in operations:
        print("These are the available operations: +, -, *, /");
        operation = input("Select an operation: ");
    return operations[operation];

def get_operand():
    """Get number input for an operand"""
    operand = "";
    while not is_number(operand):
        operand = input("Enter a valid number: ");
    return float(operand);

def check_if_finished():
    """Checks to see if user is done using the calculator"""
    yes_no = { "y" : False, "n" : True };
    do_again = "";
    while do_again not in yes_no:
        do_again = input("Perform another calculation (Y, n)? ").lower();
    return yes_no[do_again];