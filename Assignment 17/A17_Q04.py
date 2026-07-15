######################################################################################################################
#
# Write a program which accept one number form user and return addition of its factors.
# Input : 12 
# Output : 16 (1+2+3+4+6) 
#
######################################################################################################################

import math

def AddFactors(No):
    Ans = 0
    
    for i in range (1, (math.isqrt(No)+1)):
        if(No % i == 0):
            Ans += i

            partner = No // i       # Since factors always come in pairs until squareroot...eg. 1*36, 2*18....6*6

            if (i != partner and partner != No):
                Ans += partner

    return Ans

def main():

    Value1 = int(input("Enter the number : "))

    Ret = AddFactors(Value1)

    print("The addition of factors of given number is : ",Ret)

if __name__ == "__main__":
    main()