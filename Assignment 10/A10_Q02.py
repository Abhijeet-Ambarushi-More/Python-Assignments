###########################################################
#
# WAP which accepts one number and prints sum of first N
# natural numbers
# 
# Input : 5
# Output : 15
#
###########################################################

def SumAllTill(No):
    Count = 1
    Sum = 0
    while(Count <= No):
        Sum = Sum + Count
        Count = Count + 1

    return Sum

def main():
    Value = int(input("Enter the number : "))

    Ret = SumAllTill(Value)
    print(Ret)

if __name__ == "__main__":
    main()