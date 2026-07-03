###########################################################
#
# Write a lambda function which accepts two numbers and
# returns multiplication
#
###########################################################

Mult = lambda No1, No2 : No1 * No2

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Mult(Value1, Value2)
    print("Multiplication is : ",Ret)

if __name__ == "__main__":
    main()