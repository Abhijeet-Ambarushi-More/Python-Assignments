###########################################################
#
# Write a lambda function using map() which accepts a list
# of numbers and returns a list of squares of each number
#
###########################################################

Square = lambda No : No * No

# Created own map() function
def mapX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)     
        Result.append(Ret)
    
    return Result

def main():
    Data = []

    Count = int(input("Enter the number of elements in the list : "))
    if(Count < 0):
        print("Invalid number of elements")
        return

    print("Enter the elements : ")
    for i in range(Count):
        no = int(input())
        Data.append(no)

    print("Data before map : ",Data)

    Mdata = list(mapX(Square,Data))
    print("Data after map : ",Mdata)

if __name__ == "__main__":
    main()