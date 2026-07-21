######################################################################################################################
#
#  Design a Python application that creates three threads named Small, Capital, and Digits. 
# • All threads should accept a string as input. 
# • The Small thread should count and display the number of lowercase characters. 
# • The Capital thread should count and display the number of uppercase characters. 
# • The Digits thread should count and display the number of numeric digits. 
# • Each thread must also display: 
#	 • Thread ID 
#	 • Thread Name 
#
######################################################################################################################
import threading

def DisplayLowerCount(Str):
    count = 0

    for i in Str:
        if (i >= "a" and i <= "z"):
            count += 1

    print(
    "\nThread ID :", threading.get_ident(),
    "\nThread Name :", threading.current_thread().name,
    "\nNumber of the lowercase characters : ", count
    )


def DisplayUpperCount(Str):
    count = 0

    for i in Str:
        if (i >= "A" and i <= "Z"):
            count += 1
    print(
    "\nThread ID : ", threading.get_ident(),
    "\nThread Name : ", threading.current_thread().name,
    "\nNumber of the uppercase characters : ", count
    )

def DisplayDigitCount(Str):
    count = 0

    for i in Str:
        if (i >= "0" and i <= "9"):
            count += 1
    print(
    "\nThread ID :", threading.get_ident(),
    "\nThread Name :", threading.current_thread().name,
    "\nNumber of the digits : ", count
    )
    
def main():
    value = input("Enter the string : ")

    t1 = threading.Thread(target=DisplayLowerCount,name="small",args=(value,))
    t2 = threading.Thread(target=DisplayUpperCount,name="capital",args=(value,))
    t3 = threading.Thread(target=DisplayDigitCount,name="digit",args=(value,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()