######################################################################################################################
#
# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, 
# Mult() for multiplication and Div() for division. 
# All functions accepts two parameters as number and perform the operation. 
# Write on python program which call all the functions from 
# Arithmetic module by accepting the parameters from user. 
#
######################################################################################################################

import Arithmetic

def main():

    Value1 = int(input("Enter the first number : "))

    Value2 = int(input("Enter the second number : "))

    Ret = Arithmetic.Add(Value1,Value2)
    print("Addition is :",Ret)

    Ret = Arithmetic.Sub(Value1,Value2)
    print("Substraction is :",Ret)

    Ret = Arithmetic.Mult(Value1,Value2)
    print("Multiplication is :",Ret)

    Ret = Arithmetic.Div(Value1,Value2)
    print("Division is :",Ret)

if __name__ == "__main__":
    main()