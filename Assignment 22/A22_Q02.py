######################################################################################################################
#
# Write a program that calculates factorials of multiple numbers simultaneously using Pool.map(). 
# Input
# [10,15,20,25] 
# 
# Display
# • Process ID 
# • Input Number 
# • Factorial  
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
        print("PID : ",pid,"\t", number, " : ", fact)

if __name__ == "__main__":
    main()