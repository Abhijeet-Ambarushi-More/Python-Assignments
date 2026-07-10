###########################################################
#
# WAP which  contains one function that accepts a 
# number from user and returns True if number is divisible
# by 5 otherwise return False
#
# Input : 8         Output : False
# Input : 25        Output : True
#
###########################################################

def ChkNUm(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    Ret = ChkNUm(Value)

    if(Ret == True):
       print("True")
    else:
       print("False")

if __name__ == "__main__":
    main()