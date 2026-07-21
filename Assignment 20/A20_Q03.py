######################################################################################################################
#
# Design a Python application that creates two threads named EvenList and OddList. 
# • Both threads should accept a list of integers as input. 
# • The EvenList thread should: 
# 	 • Extract all even elements from the list. 
#	 • Calculate and display their sum. 
# • The OddList thread should: 
#	 • Extract all odd elements from the list. 
#	 • Calculate and display their sum. 
# • Threads should run concurrently. 
#
######################################################################################################################
import threading

def ListSumEven(lst):
    total = 0
    EvenLst = list()

    for no in lst:
        if(no%2 == 0):
            EvenLst.append(no)

    print("Even numbers in the list are : ",EvenLst)

    for i in EvenLst:
        total += i
    
    print("The sum of Even numbers in the list is  : ",total)

def ListSumOdd(lst):
    total = 0
    OddLst = list()

    for no in lst:
        if(no%2 != 0):
            OddLst.append(no)
        
    print("Odd numbers in the list are : ",OddLst)

    for i in OddLst:
        total += i
    
    print("The sum of Odd numbers in the list is  : ",total)

def main():
    Data = list()

    print("Enter values one by one (press enter when finished) : ")

    while True:
        value = input()
        if value == "":
            break
        Data.append(int(value))

    t1 = threading.Thread(target=ListSumEven,name="EvenList",args=(Data,))
    t2 = threading.Thread(target=ListSumOdd,name="OddList",args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()