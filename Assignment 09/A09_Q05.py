###########################################################
#
# WAP which accepts one number and checks whether its 
# divisible by 3 and 5
# 
# Input : 15
# Output : Divisible by 3 and 5
#
###########################################################

def DivBy3And5(No):
    if((No % 3 == 0) and (No %5 == 0)):
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    Ret = DivBy3And5(Value)
    
    if(Ret == True):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()