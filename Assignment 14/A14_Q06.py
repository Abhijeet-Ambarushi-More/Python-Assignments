###########################################################
#
# Write a lambda function which accepts one numbers and
# returns True if number is odd otherwise False 
#
###########################################################

ChkEven = lambda No : True if(No % 2 == 1) else False

def main():
    Value = int(input("Enter the first number : "))

    Ret = ChkEven(Value)
    if (Ret == True):
        print("Given number is an Odd number")
    else:
        print("Given number is Not an Odd number")

if __name__ == "__main__":
    main()