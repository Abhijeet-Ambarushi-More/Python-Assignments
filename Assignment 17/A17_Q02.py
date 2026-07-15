######################################################################################################################
#
# Write a program which accept one number and display below pattern. 
# Input : 5
# Output :  *   *   *   *   *
#           *   *   *   *   *
#           *   *   *   *   *
#           *   *   *   *   *
#           *   *   *   *   *
#
######################################################################################################################

import Arithmetic

def DisplayPattern(No):
    for i in range(No):
        print("*"*No)

def main():

    Value1 = int(input("Enter the number : "))

    DisplayPattern(Value1)


if __name__ == "__main__":
    main()