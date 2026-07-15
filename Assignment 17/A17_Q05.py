######################################################################################################################
#
# Write a program which accept one number for user and check whether number is prime or not.
# Input : 5
# Output : It is a prime number
#
######################################################################################################################

import math

def CheckPrime(No):
    Ans = True

    for i in range (2, (math.isqrt(No)+1)):

        if(No % i == 0):
            Ans = False

            

    return Ans

def main():

    Value1 = int(input("Enter the number : "))

    Ret = CheckPrime(Value1)

    if (Ret == True):
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()