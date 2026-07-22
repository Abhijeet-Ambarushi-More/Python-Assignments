######################################################################################################################
#
# Write a Python program using multiprocessing. Pool to calculate the sum of all odd numbers from 1 to N.
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# 
# Expected Task
# For each number N, calculate:
# 1+ 3 + 5+......+N
# 
# Expected Output Format
# Process ID : 1235
# Input Number : 1000000
# Sum of Odd Numbers : 250000000000
#
######################################################################################################################
import multiprocessing
import os

def SumOdd(no):
    total = 0

    for i in range(1,no+1,2):
                total += i

    return os.getpid(),no,total

def main():
    data = list()
    
    print("Enter values one by one (press enter when finished) : ")
    
    while True:
        value = input()
        if value == "":
            break
        data.append(int(value))

    pobj = multiprocessing.Pool()

    Mdata = pobj.map(SumOdd,data)

    pobj.close()
    pobj.join()

    for pid, number, total in Mdata:
        print("\nProcess ID : ",pid, "\nInput Number : ",number, "\nSum of Odd Numbers : ", total,"\n")

if __name__ == "__main__":
    main()