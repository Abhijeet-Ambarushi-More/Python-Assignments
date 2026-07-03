###########################################################
#
# WAP which accepts one number and prints square of that 
# number
# 
# Input : 5
# Output : 25
#
###########################################################

def Square(No):
    Sqr = No * No
    return Sqr

def main():
    Value = int(input("Enter the number : "))

    Ret = Square(Value)
    print(Ret)

if __name__ == "__main__":
    main()