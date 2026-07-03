###########################################################
#
# WAP which accepts one number and print sum of digits in
# that number
# 
# Input : 123
# Output : 6
#
###########################################################

def SumDigits(No):
    Sum  = 0
    Digit = 0

    while(No > 0 ):           
        Digit = No % 10
        Sum = Sum + Digit
        No = int(No / 10)      # typecasted because if values come in decimal No will be changed to float

    return Sum


def main():
    Value = int(input("Enter the number : "))

    Ret = SumDigits(Value)
    print(Ret)

if __name__ == "__main__":
    main()