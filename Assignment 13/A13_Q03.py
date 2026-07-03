###########################################################
#
# WAP which accepts one number and checks whether it is 
# perfect number or not
# 
# Input : 6
# Output : Perfect Number
#
###########################################################

def DisplayFactors(No):
    Sum = 0
    if(No % 2 == 0):       # As all prefect numbers are even, reducing time complexity by half
        for i in range(1,No):
            if(No % i == 0):
                Sum = Sum + i
    else:
        return False

    if (Sum == No):
        return True
    else:
        return False


def main():
    Value = int(input("Enter the number : ")) 

    Ret = DisplayFactors(Value)

    if(Ret == True):
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

if __name__ == "__main__":
    main()