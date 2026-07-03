###########################################################
#
# WAP which accepts radius of circle and print are of cicle
# 
# Input : 5
# Output : 5 4 3 2 1  
#
###########################################################

def RectArea(Rad):
    return (3.14159 * Rad * Rad)

def main():
    Value = int(input("Enter the Radius : "))

    Ret = RectArea(Value)
    print("The area of circle is  : ",Ret)

if __name__ == "__main__":
    main()