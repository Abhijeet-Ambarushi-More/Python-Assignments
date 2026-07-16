######################################################################################################################
#
# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List. 
# Input : 
# Number of elements : 7 
# Input Elements : 13 5 45 7 4 56 34 
# Output : 56

#
######################################################################################################################

def Max(Lst):
    Maximum = Lst[0]

    for i in Lst:
        if(i > Maximum):
            Maximum = i

    return Maximum


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

    Ret = Max(Data)
    print("Largest elements is : ",Ret)

if __name__ == "__main__":
    main()