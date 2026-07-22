######################################################################################################################
#
#  Design a Python application that creates two threads. 
# • Thread I should calculate and display the maximum element from an list. 
# • Thread 2 should calculate and display the minimum element from the same list. 
# • The list should be accepted from the user. 
#
######################################################################################################################
import threading

def Maximum(lst):
    max = lst[0]
    for no in lst:
        if(no > max):
            max = no
    print("Largest element in the list is : ",max)

def Minimun(lst):
    min = lst[0]
    for no in lst:
        if(no < min):
            min = no
    print("smallest element in the list is : ",min)

def main():
    data = list()
    
    print("Enter values one by one (press enter when finished) : ")
    
    while True:
        value = input()
        if value == "":
            break
        data.append(int(value))

    t1 = threading.Thread(target=Maximum,name="Thread 1",args=(data,))
    t2 = threading.Thread(target=Minimun,name="Thread 2",args=(data,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()