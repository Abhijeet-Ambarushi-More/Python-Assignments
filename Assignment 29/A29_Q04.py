######################################################################################################################
#
# Compare Two Files(Command line)
# 
# problem statement : 
# wap which accepts two file names through command line arguments and compare the contents of both files
# • If the both files contains same contents, display Success
# • Otherwise display Failure
#
# Input(Command line) :
# Marvellous.txt    Demo.txt
#
# Expected output : 
# Success or Failure
#
######################################################################################################################
import sys

def main():
    try:
        if(len(sys.argv) == 3):
            FileName1 = (sys.argv[1])
            FileName2 = (sys.argv[2])

            fd1 = open(FileName1,"r",encoding="cp1252")

            data1 = fd1.read()

            fd2 = open(FileName2,"r")

            data2 = fd2.read()

            fd1.close()
            fd2.close()

            if(data1 == data2):
                print("Success")
            else:
                print("Failure")

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()