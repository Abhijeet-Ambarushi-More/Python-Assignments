###########################################################
#
# Write a lambda function using reduce() which accepts a 
# list of numbers and returns the addition of all elements
#
###########################################################

Add = lambda No1, No2 : No1 + No2

# Created own reduce() function
def reduceX(Task, Elements):
    Sum = 0

    for no in Elements:
        Sum = Task(Sum, no)
        
    return Sum

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

    print("Data before reduce : ",Data)

    Rdata = reduceX(Add,Data)
    print("Data after reduce : ",Rdata)

if __name__ == "__main__":
    main()