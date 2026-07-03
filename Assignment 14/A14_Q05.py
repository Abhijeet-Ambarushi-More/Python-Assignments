###########################################################
#
# Write a lambda function which accepts one numbers and
# returns True if number is even otherwise False 
#
###########################################################

ChkEven = lambda No : True if(No % 2 == 0) else False

def main():
    Value = int(input("Enter the first number : "))

    Ret = ChkEven(Value)
    if (Ret == True):
        print("Given number is an Even number")
    else:
        print("Given number is Not an Even number")

if __name__ == "__main__":
    main()