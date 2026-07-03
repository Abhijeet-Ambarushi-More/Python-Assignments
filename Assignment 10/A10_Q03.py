###########################################################
#
# WAP which accepts one number and prints factorial of that
# number
# 
# Input : 5
# Output : 120
#
###########################################################

def Factorial(No):
    Count = 1
    Fact = 1
    while(Count <= No):
        Fact = Fact * Count
        Count = Count + 1

    return Fact

def main():
    Value = int(input("Enter the number : "))

    Ret = Factorial(Value)
    print(Ret)

if __name__ == "__main__":
    main()