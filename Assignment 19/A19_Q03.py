######################################################################################################################
#
# Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. 
# Map function will increase each number by 10. 
# Reduce will return product of all that numbers.
#  
# Input List = [4, 34, 36, 76, 68, 24, 89, 23 ,86, 90, 45, 70] 
# List after filter = [76, 89, 86, 90, 70] 
# List after map = [86, 99, 96, 100, 80] 
# Output of reduce = 6538752000
#
######################################################################################################################
from functools import reduce

ChkRange = lambda No: No>=70 and No<=90

Add10 = lambda No: No+10

Mult = lambda No1,No2 : No1 * No2 

def main():
    Data = []

    Count = int(input("Enter number of elements : "))

    print("Enter the elements : ")

    for i in range(Count):
        Value = int(input())
        Data.append(Value)

    # we can replace code from line 25 to 33 with following line if we want
    # Data = [int(x) for x in input("Enter the elements: ").split()]
    # but in this way we have to give input separated by spaces, unlike the current method of separating by pressing enter

    print("Actual Data before operation:",Data)

    FData = list(filter(ChkRange,Data))
    print("List after filter = ",FData)

    MData = list(map(Add10,FData))
    print("List after map = ",MData)

    RData = reduce(Mult, MData)
    print("Output of reduce = ",RData)

if __name__ == "__main__":
    main()