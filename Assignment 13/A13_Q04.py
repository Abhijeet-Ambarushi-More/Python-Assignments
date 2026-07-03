###########################################################
#
# WAP which accepts one number and prints its binary 
# equivalent
#
###########################################################

def DisplayBinary(No):
    Bin = ""

    while(No != 0):
        Digit = No % 2
        Bin = str(Digit) + Bin
        No = No//2      # floor division removes the decimal value after div and give int output

    return Bin

def main():
    Value = int(input("Enter the number : ")) 

    Ret = DisplayBinary(Value)
    print("Binary equvivalent of given number is : ",Ret)

if __name__ == "__main__":
    main()