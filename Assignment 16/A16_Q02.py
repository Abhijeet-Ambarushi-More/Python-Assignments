###########################################################
#
# WAP which contains one function named as ChkNum() which 
# accepts one parameter as a number. If the number is 
# even then it should display "Even number" otherwise 
# display "Odd number" on console.
#
# Input : 11        Output : Odd number
# Input : 8         Output : Even number
#
###########################################################

def ChkNum(No):

    if(No%2 == 0):
        return True
    else:
        return False

def main():

    Value = 0
    Ret = False

    Value = int(input("Enter the number : "))

    Ret = ChkNum(Value)

    if(Ret == True):
        print("Even Number")

    else:
        print("Odd Number")

if __name__ == "__main__":
    main()