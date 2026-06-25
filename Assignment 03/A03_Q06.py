###########################################################
#
# WAP to Display:
#
# Data type
# Memory address
# Size in bytes
# of a variable entered by user
#
###########################################################

from sys import getsizeof

def main():
    dtype = input("Enter type (int/float/string): ")
    x = input("Enter value: ")

    if dtype == "int":
        x = int(x)
    elif dtype == "float":
        x = float(x)

    print(type(x))
    print(id(x))
    print(getsizeof(x))

if __name__ == "__main__":
    main()