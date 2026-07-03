###########################################################
#
# Write a lambda function which accepts two numbers and
# returns minimum number
#
###########################################################

Minimun = lambda No1, No2 : No1 if(No1 < No2) else No2

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Minimun(Value1, Value2)
    print(Ret,"is the smaller number")

if __name__ == "__main__":
    main()