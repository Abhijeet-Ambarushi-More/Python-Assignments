######################################################################################################################
#
#  Design a Python application that creates two threads named EvenFactor and OddFactor. 
# • Both threads should accept one integer number as a parameter 
# • The EvenFactor thread should: 
# 	 • Identify all even factors of the given number. 
#	 • Calculate and display the sum of even factors. 
# • The OddFactor thread should: 
#	 • Identify all odd factors of the given number. 
#	 • Calculate and display the sum of odd factors. 
# • After both threads complete execution, the main thread should display the message: 
#   "Exit from main" 
#
#
######################################################################################################################
import threading

def SumEvenFact(no):
    total = 0

    for i in range(2, no+1, 2):
        if(no%i == 0):
            total += i
    
    print("The sum of Even factors is  : ",total)

def SumOddFact(no):
    total = 0

    for i in range(1, no+1, 2):
        if(no%i == 0):
            total += i
            
    print("The sum of Odd factors is  : ",total)

def main():
    value = int(input("Enter the number to find its factors : "))
    t1 = threading.Thread(target=SumEvenFact,name="EvenFactor",args=(value,))
    t2 = threading.Thread(target=SumOddFact,name="OddFactor",args=(value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()