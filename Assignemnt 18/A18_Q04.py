######################################################################################################################
#
# Write a program which accept N numbers from user and store it into List. 
# Accept one another number from user and return frequency of that number from List. 
# Input : Number of elements : 11 
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65 
# Element to search : 5 
# Output : 3
#
######################################################################################################################

def Frequency(Lst, No):
    Freq = 0

    for i in Lst:
        if( i == No):
            Freq += 1

    return Freq


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

    Value2 = int(input("Enter the elements to search: "))

    Ret = Frequency(Data, Value2)
    print("Frequency of the given element is : ",Ret)

if __name__ == "__main__":
    main()