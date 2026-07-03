###########################################################
#
# WAP which accepts one number and prints all even numbers
# till that number
# 
# Input : 10
# Output : 2    4   6   8   10
#
###########################################################

def PrintEvenTill(No):
    for i in range(2,(No+1)):
        if(i % 2 == 0):
            print(i,end = "   ")

def main():
    Value = int(input("Enter the number : "))

    PrintEvenTill(Value)

if __name__ == "__main__":
    main()