######################################################################################################################
#
# Write a program that accepts a list of integers and uses Pool.map() 
# to calculate the sum of squares from 1 to N for every element in the list. 
# Example Input 
# [1000000,2000000,3000000,4000000]
#
# Expected Output 
# [333333833333500000, 2666668666667000000, ...] 
#
######################################################################################################################
import multiprocessing

def SumSquare(no):
    ans = 0

    for i in range(1,no+1):
            ans += i**2

    return ans

def main():
    data = list()
    
    print("Enter values one by one (press enter when finished) : ")
    
    while True:
        value = input()
        if value == "":
            break
        data.append(int(value))

    pobj = multiprocessing.Pool()

    Mdata = pobj.map(SumSquare,data)

    pobj.close()
    pobj.join()

    print("Result is : ",Mdata)

if __name__ == "__main__":
    main()