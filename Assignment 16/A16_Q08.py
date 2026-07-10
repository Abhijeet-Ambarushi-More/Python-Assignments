###########################################################
#
# WAP which accepts a number from user and print that 
# number of "*" on screen
#
###########################################################

def Display(No):
    print(No*"*\t")

def main():
    Value = int(input("Enter the number : "))

    Display(Value)

if __name__ == "__main__":
    main()