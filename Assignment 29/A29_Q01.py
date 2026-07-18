######################################################################################################################
#
# Check file exist in current directory
# 
# problem statement : 
# wap which accepts a file name from the user and checks whether that file exists in current directory or not
#
# Input :
# Marvellous.txt
#
# Expected output : 
# Display whether Marvellous.txt exists or not 
#
######################################################################################################################
import os

def main():
    FileName = input("Enter the file name: ")

    if(os.path.exists(FileName)):
        print("File present in current directory")
    else:
        print("No such file in the directory")

if __name__ == "__main__":
    main()