######################################################################################################################
#
# Write a program that counts how many even numbers exist between 1 and N using Pool.map().
# 
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# 
# Expected Output Format
# Process ID : 1236
# Input Number : 1000000
# Even Number Count : 500000
#
######################################################################################################################
import multiprocessing
import os

def CountEven(no):
    count = 0

    for i in range(2,no+1,2):
                count += 1

    return os.getpid(),no,count

def main():
    data = list()
    
    print("Enter values one by one (press enter when finished) : ")
    
    while True:
        value = input()
        if value == "":
            break
        data.append(int(value))

    pobj = multiprocessing.Pool()

    Mdata = pobj.map(CountEven,data)

    pobj.close()
    pobj.join()

    for pid, number, count in Mdata:
        print("\nProcess ID : ",pid, "\nInput Number : ",number, "\nEven Number Count : ", count,"\n")

if __name__ == "__main__":
    main()