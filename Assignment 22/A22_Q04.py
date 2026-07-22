######################################################################################################################
#
# Write a program that calculates
#
# 1^5+2^5+3^5+....+N^5
#
# for multiple values of N simultaneously using Pool.
#
# Input

# [1000000,
# 2000000,
# 3000000, 
# 4000000]
#
# Measure total execution time. 
#
######################################################################################################################
import multiprocessing
import time

def SumPower5(no):
    ans = 0

    for i in range(1,no+1):
            ans += i**5

    return ans

        

def main():
    data = list()
    
    print("Enter values one by one (press enter when finished) : ")
    
    while True:
        value = input()
        if value == "":
            break
        data.append(int(value))

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumPower5,data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is : ")
    print(Result)

    print(f"Time required : {end_time-start_time:.4f}")

if __name__ == "__main__":
    main()