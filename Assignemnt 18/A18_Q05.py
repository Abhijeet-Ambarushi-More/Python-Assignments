######################################################################################################################
#
# Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. 
# Main python file accepts N numbers from user and pass each number to ChkPrime() function 
# which is part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime(). 
# Input : 
# Number of elements : 11 
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8 
# Output : 32 (13 + 5 + 7 +2 + 5)
#
######################################################################################################################

import MarvellousNum

def ListPrime(Lst):
    Sum = 0

    for i in Lst:
        Sum += i

    return Sum


def main():
    Data = []
    Ret = 0

    Count = int(input("Enter Number of elements : "))

    if(Count <= 0):
        print("Invalid number of elements")
        return

    print("Enter the elements : ")
    for i in range(Count):
        Value = int(input())
        Data.append(Value)

    PData = MarvellousNum.ChkPrime(Data)

    Ret = ListPrime(PData)
    print("Addition of the prime elements in the given list is : ",Ret)

if __name__ == "__main__":
    main()