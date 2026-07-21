######################################################################################################################
#
#  Design a Python application that creates two threads named Thread1 and Thread2. 
# • Thread1 should display numbers from 1 to 50. 
# • Thread2 should display numbers from 50 to 1 in reverse order. 
# • Ensure that 
#	 • Thread2 starts execution only after Thread1 has completed. 
# • Use appropriate thread synchronization
#
######################################################################################################################
import threading

def Display(no):
    print("Numbers from 1 to",no,": ")
    for i in range(1,no+1):
        print(i)

def DisplayReverse(no):
    print("Numbers from",no,"to 1 : ")
    for i in range(no, 0, -1):
        print(i)

def main():
    value = int(input("Enter the number : "))

    t1 = threading.Thread(target=Display,name="Thread1",args=(value,))
    t2 = threading.Thread(target=DisplayReverse,name="Thread2",args=(value,))

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()