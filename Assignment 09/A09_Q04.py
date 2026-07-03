###########################################################
#
# WAP which accepts one number and prints cube of that 
# number
# 
# Input : 5
# Output : 125
#
###########################################################

def Cube(No):
    Cb = No * No * No
    return Cb

def main():
    Value = int(input("Enter the number : "))

    Ret = Cube(Value)
    print(Ret)

if __name__ == "__main__":
    main()