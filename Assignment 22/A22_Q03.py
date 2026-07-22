######################################################################################################################
#
# For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing Pool. 
# Example 
#
# 10000 
# 20000 
# 30000 
# 40000 
# 
# Display total prime count for each number. 
#
######################################################################################################################
import multiprocessing
import math

def IsPrime(No):

    if No < 2:
        return False

    for i in range(2, math.isqrt(No) + 1):
        if No % i == 0:
            return False

    return True

def CountPrime(no):
    count = 0

    for i in range(2, no + 1):
        if IsPrime(i):
            count += 1
        
    return count

        

def main():
    data = list()
    
    print("Enter values one by one (press enter when finished) : ")
    
    while True:
        value = input()
        if value == "":
            break
        data.append(int(value))

    pobj = multiprocessing.Pool()

    Mdata = pobj.map(CountPrime,data)

    print(Mdata)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()