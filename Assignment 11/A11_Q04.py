###########################################################
#
# WAP which accepts one number and print reverse of that
# number
# 
# Input :  123
# Output : 321
#
###########################################################

def SumDigits(No):
    Sum  = 0
    Digit = 0

    while(No > 0 ):          
        Digit = No % 10
        print(Digit,end="")
        No = int(No / 10)   


def main():
    Value = int(input("Enter the number : "))

    SumDigits(Value)

if __name__ == "__main__":
    main()