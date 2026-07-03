###########################################################
#
# WAP which accepts one number and prints multiplication 
# table of that number
# 
# Input : 4
# Output : 4 8 12 16 20 24 28 32 36 40
#
###########################################################


# Attempt to keep input and output in main function
def MultTable(No):
    Table = [0] * 10
    for i in range(len(Table)):
        Table[i] = 4 * (i+1)

    return Table

def main():
    Value = int(input("Enter the number : "))

    Ret = MultTable(Value)

    for j in range(10):         # end of range will be always 10 because we want table
        print(Ret[j],end="    ")
        
if __name__ == "__main__":
    main()