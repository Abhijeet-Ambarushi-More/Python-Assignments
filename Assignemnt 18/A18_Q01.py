######################################################################################################################
#
# Write a program which accept N numbers from user and store it into List.
# Return addition of all elements from that List. 
# Input : 
# Number of elements : 6 
# Input Elements : 13 5 45 7 4 56 
# Output : 130
#
######################################################################################################################

def Addition(Lst):
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

    print("Enter the elements : ")
    for i in range(Count):
        Value = int(input())
        Data.append(Value)

    Ret = Addition(Data)
    print("Addition of elements is : ",Ret)

if __name__ == "__main__":
    main()