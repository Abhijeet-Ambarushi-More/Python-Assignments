######################################################################################################################
#
# Design a Python application that creates two separate threads named Even and Odd. 
# • The Even thread should display the first 10 even numbers. 
# • The Odd thread should display the first 10 odd numbers. 
# • Both threads should execute independently using the threading module. 
# • Ensure proper thread creation and execution. 
#
######################################################################################################################
import threading

def DisplayEven(Count):
    print("Even Numbers : ")
    for i in range(2, (Count*2)+1, 2):
        print(i)

def DisplayOdd(Count):
    print("Odd Numbers : ")
    for i in range(1, (Count*2)+1, 2):
        print(i)

def main():
    Value = int(input("Enter the number : "))
    t1 = threading.Thread(target=DisplayEven,name="Even",args=(Value,))
    t2 = threading.Thread(target=DisplayOdd,name="Odd",args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()



if __name__ == "__main__":
    main()