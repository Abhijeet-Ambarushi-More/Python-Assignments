######################################################################################################################
#
# Write a program which accept number from user and return addition of digits in that number. 
# Input : 5187934 
# Output : 37  
#
#
######################################################################################################################

import math

def CountDigits(No):
    Digit = 0
    Sum = 0

    while(No != 0):
        Digit = No % 10
        No = No // 10
        Sum += Digit
    
    return Sum

def main():

    Value = int(input("Enter the number : "))

    Ret = CountDigits(Value)
    print(Ret)

if __name__ == "__main__":
    main()