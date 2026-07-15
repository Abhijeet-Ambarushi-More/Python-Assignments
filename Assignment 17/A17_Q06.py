######################################################################################################################
#
# Write a program which accept one number and display below pattern.
# Input : 5
# Output :  *   *   *   *   *
#           *   *   *   *
#           *   *   *
#           *   *   
#           *
#
######################################################################################################################
def DisplayPattern(No):
    for i in range(No): 
        for j in range(No): 
            if(i<=j):
                print("*",end= "   ")

        print()

def main():

    Value = int(input("Enter the number : "))

    DisplayPattern(Value)

if __name__ == "__main__":
    main()
