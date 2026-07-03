###########################################################
#
# WAP which accepts one number and checks whether its prime
# or not
# 
# Input : 11
# Output : Prime Number
#
###########################################################

def CheckPrime(No):
    for i in range(2,No):
        if(No % i == 0):
            return False
        else:
            return True

def main():
    Value = int(input("Enter the number : "))

    Ret = CheckPrime(Value)
    if (Ret == True):
        print("Prime Number")
    else:
        print("Not A Prime Number")

if __name__ == "__main__":
    main()