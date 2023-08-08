import sys

# -------------------------------------------------------- #
# -- MAIN FUNCTIONAILTY -- DO NOT EDIT ------------------- #
# -------------------------------------------------------- #

a = None
b = None
op = None

# Add function
# a -- argument 1
# b -- argument 2
def add(a, b):
    return a + b

while (True):
    # get input values
    a =  input("Enter the first numeric argument or [q] to exit: ")
    if (str(a) == 'q'):
        exit()

    op = input("Enter the operation [+,-,*,/,q (exit)]: ")

    if str(op) == 'q':
        exit()

    b =  input("Enter the second numeric argument or [q] to exit:  ")

    if str(b) == 'q':
        exit()

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Invalid number argument...")
        op = None

                    # decide function
    if (op != None):
        if (op == "+"):
            print ("Sum:: ", add(a, b))
        elif (op == "-"):
            print("Difference:")
        elif (op == "*"):
            print("Product:")
        elif (op == "/"):
            print("Quotient:")
        else:
            print("Invalid operation...")