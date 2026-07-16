######################################################################################################################
#
# Write a program which contains one lambda function which accepts two parameters and return its multiplication. 
# Input : 4    3    Output : 12 
# Input : 6    3    Output : 18
#
######################################################################################################################
PowerTwo = lambda No1, No2: No1*No2

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = PowerTwo(Value1, Value2)

    print("Multipplication is : ",Ret)

if __name__ == "__main__":
    main()