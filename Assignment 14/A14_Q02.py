###########################################################
#
# Write a lambda function which accepts one number and
# returns cube of that number
#
###########################################################

Cube = lambda No : No ** 3            # 3 is the power here

def main():
    Value = int(input("Enter the number : ")) 

    Ret = Cube(Value)
    print("Cube : ",Ret)

if __name__ == "__main__":
    main()