######################################################################################################################
#
# Write a program which accept N numbers from user and store it into List. Return Minimum number from that List. 
# Input : 
# Number of elements : 4 
# Input Elements : 13 5 45 7
# Output : 5

#
######################################################################################################################

def Min(Lst):
    Mininmum = Lst[0]

    for i in Lst:
        if(i < Mininmum):
            Mininmum = i

    return Mininmum


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

    Ret = Min(Data)
    print("Smallest elements is : ",Ret)

if __name__ == "__main__":
    main()