import sys

# -------------------------------------------------------- #
# -- MAIN FUNCTIONAILTY -- DO NOT EDIT ------------------- #
# -------------------------------------------------------- #

a = None
b = None
op = None

while (True):
    # get input values
    a =  input("Enter the first argument: ")
    op = input("Enter the operation: ")
    b =  input("Enter the second argument: ")

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Invalid number argument...")
        op = None