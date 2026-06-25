###########################################################
#
# WAP that accepts two number from user and prints their
# Addition
# Substraction
# Multiplication
# Division
#
###########################################################


def Arithmatic(No1,No2):

    Add = No1 + No2
    Sub = No1 - No2
    Mult = No1 * No2
    Div = No1 / No2

    return Add,Sub,Mult,Div

def main():
    Value1 = int(input("Enter First Number : "))
    Value2 = int(input("Enter Second Number : "))

    ret1,ret2,ret3,ret4 = Arithmatic(Value1, Value2)

    print("Addition is : ",ret1)
    print("Substraction is : ",ret2)
    print("Multiplication is : ",ret3)
    print("Division is : ",ret4)
    

if __name__ == "__main__":
    main()