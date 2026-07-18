######################################################################################################################
#
# Copy file contents into a new file (Command line)
# 
# problem statement : 
# wap which accepts an existing file name throught command line arguments and create new file named Demo.txt and 
# copies all contents from the given file into Demo.txt
#
# Input(Command line) :
# Marvellous.txt
#
# Expected output : 
# Display contents of Marvellous.txt on console
#
######################################################################################################################
import sys

def main():
    try:
        if(len(sys.argv) == 3):
            FileName1 = (sys.argv[1])

            fd1 = open(FileName1,"r",encoding="cp1252")

            data1 = fd1.read()

            fd2 = open("Demo.txt","a+")

            fd2.write(data1)

            fd2.seek(0)

            data2 = fd2.read()
            print("Contents of ",FileName1," into Demo.txt : \n",data2)

            fd1.close()
            fd2.close()
        else:
            print("Invalid number of arguments\n")

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()