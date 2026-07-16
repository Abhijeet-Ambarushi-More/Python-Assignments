######################################################################################################################
#
# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. 
# Reduce will return Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions). 
#
#Input List = [2, 70 , 11, 10, 17, 23, 31, 77] 
#List after filter = [2, 11, 17, 23, 31] 
#List after map = [4, 22, 34, 46, 62] 
#Output of reduce = 62
#
######################################################################################################################
import math
from functools import reduce

def CheckPrime(No):

    if No < 2:
        return False

    for i in range(2, math.isqrt(No) + 1):
        if No % i == 0:
            return False

    return True

# we can also convert it into lambda but but I would prefer a regular function because the logic is clearer and easier to maintain.
# CheckPrime = lambda n: (n >= 2 and all(n % i != 0 for i in range(2, math.isqrt(n) + 1)))

MultBy2 = lambda No: No*2

Max = lambda No1,No2 : No1 if(No1>No2) else No2

def main():
    Data = []

    Count = int(input("Enter number of elements : "))

    print("Enter the elements : ")

    for i in range(Count):
        Value = int(input())
        Data.append(Value)

    # we can replace code from line 39 to 47 with following line if we want
    # Data = [int(x) for x in input("Enter the elements: ").split()]
    # but in this way we have to give input separated by spaces, unlike the current method of separating by pressing enter

    FData = list(filter(CheckPrime,Data))
    print("List after filter = ",FData)

    MData = list(map(MultBy2,FData))
    print("List after map = ",MData)

    RData = reduce(Max, MData)
    print("Output of reduce = ",RData)

if __name__ == "__main__":
    main()