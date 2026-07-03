###########################################################
#
# Write a lambda function using filter() which accepts a 
# list of numbers and returns the count of even numbers
#
###########################################################

ChkEven = lambda No : True if (No % 2 == 0) else False

# Created own filter() function
def filterX(Task, Elements):
    Count = 0

    for no in Elements:
        Ret = Task(no)      
        if(Ret == True):
            Count = Count + 1

    return Count

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

    Fdata = filterX(ChkEven,Data)
    print("Data after filter : ",Fdata)

if __name__ == "__main__":
    main()