######################################################################################################################
#
# Write a Python program using multiprocessing. Pool 
# to calculate the sum of all even numbers from 1 to N for every number from the given list.
#
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
#
# Expected Task
# For each number N, calculate:
# 2+4+6+......+ N
#
# Expected Output Format
# Process ID : 1234
# Input Number : 1000000
# Sum of Even Numbers : 250000500000
#
######################################################################################################################
import multiprocessing
import os

def SumEven(no):
    total = 0

    for i in range(2,no+1,2):
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

    Mdata = pobj.map(SumEven,data)

    pobj.close()
    pobj.join()

    for pid, number, total in Mdata:
        print("\nProcess ID : ",pid, "\nInput Number : ",number, "\nSum of Even Numbers : ", total,"\n")

if __name__ == "__main__":
    main()