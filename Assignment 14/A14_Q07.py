###########################################################
#
# Write a lambda function which accepts one numbers and
# returns True if divisible by 5
#
###########################################################

ChkEven = lambda No : True if(No % 5 == 0) else False

def main():
    Value = int(input("Enter the first number : "))

    Ret = ChkEven(Value)
    if (Ret == True):
        print("Given number is divisible by 5")
    else:
        print("Given number is Not divisible by 5")

if __name__ == "__main__":
    main()