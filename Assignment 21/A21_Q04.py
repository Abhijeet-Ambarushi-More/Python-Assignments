######################################################################################################################
#
#  Design a Python application that creates two threads. 
# • Thread 1 should compute the sum of elements from a list. 
# • Thread 2 should compute the product of elements from the same list. 
# • Return the results to the main thread and display them. 
#
######################################################################################################################
import threading

sum_result = 0
product_result = 1

def AddList(lst):
    global sum_result
    
    for no in lst:
        sum_result += no

def MultList(lst):
    global product_result
    for no in lst:
        product_result = product_result * no

def main():
    data = list()
    
    print("Enter values one by one (press enter when finished) : ")
    
    while True:
        value = input()
        if value == "":
            break
        data.append(int(value))

    t1 = threading.Thread(target=AddList,name="Thread 1",args=(data,))
    t2 = threading.Thread(target=MultList,name="Thread 2",args=(data,))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    print("Addition of the elements in the list is : ",sum_result)
    print("product of the elements in the list is : ",product_result)


if __name__ == "__main__":
    main()