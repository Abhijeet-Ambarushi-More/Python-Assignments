######################################################################################################################
#
# Write a program which accept one number from user and return its factorial.
# Input : 5 
# Output : 120 
#
######################################################################################################################

def DisplayFactorial(No):
    Fact = 1

    for i in range(1, No+1):
        Fact = Fact * i

    return Fact

def main():

    Value1 = int(input("Enter the number : "))

    Ret = DisplayFactorial(Value1)

    print("The factorial of given number is : ",Ret)

if __name__ == "__main__":
    main()