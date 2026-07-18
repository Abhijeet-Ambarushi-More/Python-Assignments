######################################################################################################################
#
# Copy file contents into another file
# 
# problem statement : 
# wap which accepts two file name from the user 
# • First file is an existing file
# • Second file is the new file
#
# Copy all the contents of one file into the second file
#
# Input :
# Marvellous.txt    Demo.txt
#
# Expected output : 
# Contents of Marvellous.txt into Demo.txt
#
######################################################################################################################
def main():
    try:
        fd1 = open("Marvellous.txt","r",encoding="cp1252")

        data1 = fd1.read()

        fd2 = open("Demo.txt","a+")

        fd2.write(data1)

        fd2.seek(0)

        data2 = fd2.read()
        print("Contents of Marvellous.txt into Demo.txt : \n",data2)

        fd1.close()
        fd2.close()

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()