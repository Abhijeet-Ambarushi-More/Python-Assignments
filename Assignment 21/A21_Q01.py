######################################################################################################################
#
#  Design a Python application that creates two threads named Prime and NonPrime. 
# • Both threads should accept a list of integers. 
# • The Prime thread should display all prime numbers from the list. 
# • The NonPrime thread should display all non-prime numbers from the list.
#
######################################################################################################################
import threading
import math

def IsPrime(No):

    if No < 2:
        return False

    for i in range(2, math.isqrt(No) + 1):
        if No % i == 0:
            return False

    return True

def ChkPrime(Lst):
    PrimeList = []

    for i in Lst:
            if IsPrime(i):
                PrimeList.append(i)

    print("Prime elements in the list are : ",PrimeList)

def ChkNonPrime(Lst):
    NonPrimeList = []

    for i in Lst:
            if not IsPrime(i) :
                NonPrimeList.append(i)

    print("NonPrime elements in the list are : ",NonPrimeList)

def main():
    data = list()
    
    print("Enter values one by one (press enter when finished) : ")
    
    while True:
        value = input()
        if value == "":
            break
        data.append(int(value))

    t1 = threading.Thread(target=ChkPrime,name="Prime",args=(data,))
    t2 = threading.Thread(target=ChkNonPrime,name="NonPrime",args=(data,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()