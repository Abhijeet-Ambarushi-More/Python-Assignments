######################################################################################################################
#
# Count lines in a file
# 
# problem statement : 
# wap which accepts a file name from the user and counts how many lines are present in the file.
#
# Input :
# Marvellous.txt
#
# Expected output : 
# Total number of lines in Demo.txt
#
######################################################################################################################
def main():
    try:
        Count = 0

        FileName = input("Enter the file name: ")

        fd = open(FileName,"r",encoding="cp1252")

        while True:
            line = fd.readline()

            if line == "":
                break

            Count += 1

        fd.close()

        print("Total number of lines in ",FileName," : ",Count)


    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()