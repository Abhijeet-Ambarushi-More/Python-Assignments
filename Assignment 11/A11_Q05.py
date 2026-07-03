###########################################################
#
# WAP which accepts one number and checks whether it is 
# palindrome or not
# 
# Input :  121
# Output : Palindrome
#
###########################################################

def SumDigits(No):
    Digit = 0
    Before = No
    Rev = 0

    while(No > 0 ):                     
        Digit = No % 10      
        Rev = (Rev*10) + Digit           
        No = int(No / 10)               

    if (Before == Rev):
        return True
    else:
        return False


def main():
    Value = int(input("Enter the number : "))

    Ret = SumDigits(Value)
    if (Ret == True):
        print("Palindrome")
    else:
        print("Not A Palindrome")

if __name__ == "__main__":
    main()