######################################################################################################################
#
# Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.
#
# Input
# Data = [10, 15, 20, 25]
# 
# Expected Task
# For every N, calculate:
# N1
#
# Expected Output Format
# Process ID: 1240
# Input Number: 20
# Factorial : 2432902008176640000
# 
#
######################################################################################################################
import multiprocessing
import os

def Factorial(no):
    fact = 1

    for i in range(1,no+1):
            fact = fact * i

    return os.getpid(),no,fact

def main():
    data = list()
    
    print("Enter values one by one (press enter when finished) : ")
    
    while True:
        value = input()
        if value == "":
            break
        data.append(int(value))

    pobj = multiprocessing.Pool()

    Mdata = pobj.map(Factorial,data)

    pobj.close()
    pobj.join()

    for pid, number, fact in Mdata:
        print("\nProcess ID : ",pid, "\nInput Number : ",number, "\nFactorial : ", fact,"\n")

if __name__ == "__main__":
    main()