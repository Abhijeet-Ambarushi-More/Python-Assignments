###########################################################
#
# Write a lambda function using filter() which accepts a 
# list of numbers and returns a list of even number
#
###########################################################

ChkEven = lambda No : True if (No % 2 == 0) else False

# Created own filter() function
def filterX(Task, Elements):
    Result = []

    for no in Elements:
        Ret = Task(no)      
        if(Ret == True):
            Result.append(no)

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

    print("Data before filter : ",Data)

    Fdata = list(filterX(ChkEven,Data))
    print("Data after filter : ",Fdata)

if __name__ == "__main__":
    main()