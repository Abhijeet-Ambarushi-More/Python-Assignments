###########################################################
#
# WAP which accepts a number from user and check whether that 
# number is positive or negative or zero
#
# Input : 11        Output : Positive number
# Input : -8        Output : Negative number
# Input : 0         Output : Zero
#
###########################################################

def ChkNUm(No):
    if(No == 0):
        print("Zero")
    elif(No < 0):
        print("Negative number")
    else:
        print("Positive number")

def main():
   Value = int(input("Enter the number : "))

   ChkNUm(Value)


if __name__ == "__main__":
    main()