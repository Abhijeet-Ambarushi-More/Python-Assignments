######################################################################################################################
#
# Display file contents
# 
# problem statement : 
# wap which accepts a file name from the user and open that file, and display the entire contents on console
#
# Input :
# Marvellous.txt
#
# Expected output : 
# Display contents of Marvellous.txt on console
#
######################################################################################################################
def main():
    try:
        FileName = input("Enter the file name: ")

        fd = open(FileName,"r",encoding="cp1252")

        Data = fd.read()

        print(Data)

        fd.close()
       
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()