###########################################################
#
# Write a lambda function using reduce() which accepts a 
# list of numbers and returns the Minimum element
#
###########################################################

Minimum = lambda No1, No2 : No1 if(No1 < No2) else No2

# Created own reduce() function
def reduceX(Task, Elements):
    Result = Elements[0]

    for no in Elements:
        Result = Task(Result, no)
        
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

    print("Date before reduce : ",Data)

    Rdata = reduceX(Minimum,Data)
    print("Data after reduce : ",Rdata)

if __name__ == "__main__":
    main()