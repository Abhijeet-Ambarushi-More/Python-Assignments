######################################################################################################################
#
#  Design a Python application where multiple threads update a shared variable. 
# • Use a Lock to avoid race conditions. 
# • Each thread should increment the shared counter multiple times. 
# • Display the final value of the counter after all threads complete execution. 
#
######################################################################################################################
import threading

count = 0
lock = threading.Lock()

def Increment(no):
    global count

    for i in range(no):

        lock.acquire()

        count += 1
         
        lock.release()

def main():
    value = int(input("Enter the number : "))

    t1 = threading.Thread(target=Increment,name="Thread 1",args=(value,))
    t2 = threading.Thread(target=Increment,name="Thread 2",args=(value,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    global count
    print("Total count : ",count)

if __name__ == "__main__":
    main()