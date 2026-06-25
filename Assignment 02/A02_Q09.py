###########################################################
#
# WAP to take user's name and age and display:
# Hello <name>, you will turn <age+1> next year
#
###########################################################

def Arithmatic(sName,iAge):
    print("Hello", sName, "you will turn", iAge+1, "next year")

if __name__ == "__main__":
    
    sName = input("Enter your name : ")
    iAge = int(input("Enter your age : "))

    Arithmatic(sName, iAge)