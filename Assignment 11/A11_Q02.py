###########################################################
#
# WAP which accepts one number and print count of digits in
# that number
# 
# Input : 7521
# Output : 4
#
###########################################################

def CheckDigits(No):
    Digit = 0

    while(No > 0 ):            # or we can use No >= 1 , to avoid typecasting at line 15
        No = int(No / 10)      # typecasted because if values come in decimal No will be changed to float
        Digit = Digit + 1

    return Digit


def main():
    Value = int(input("Enter the number : "))

    Ret = CheckDigits(Value)
    print(Ret)

if __name__ == "__main__":
    main()