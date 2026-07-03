###########################################################
#
# WAP which accepts one number and print its factors
# 
# Input :  12
# Output : 1 2 4 6 12
#
###########################################################

def DisplayFactors(No):
    for i in range(1,(No+1)):
        if(No % i == 0):
            print(i, end = "   ")

def main():
    Value = int(input("Enter the number : ")) 

    DisplayFactors(Value)

if __name__ == "__main__":
    main()