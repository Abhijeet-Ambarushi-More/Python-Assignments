###########################################################
#
# WAP which accepts length and width of rectangle and 
# print its area
# 
# Input : 5
# Output : 5 4 3 2 1  
#
###########################################################

def RectArea(Len, Wid):
    return (Len * Wid)

def main():
    Value1 = int(input("Enter the Length : "))
    Value2 = int(input("Enter the Width : "))

    Ret = RectArea(Value1,Value2)
    print("The area of rectangle is  : ",Ret)

if __name__ == "__main__":
    main()