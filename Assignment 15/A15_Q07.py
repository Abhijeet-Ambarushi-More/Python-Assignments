###########################################################
#
# Write a lambda function using filter() which accepts a 
# list of strings and returns a list of strings having
# length greater than 5
#
###########################################################

ChkLen = lambda Str : True if (len(Str)>5) else False

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
        no = str(input())
        Data.append(no)

    print("Data before filter : ",Data)

    Fdata = list(filterX(ChkLen,Data))
    print("Data after filter : ",Fdata)

if __name__ == "__main__":
    main()