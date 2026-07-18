######################################################################################################################
#
# Count words in a file
# 
# problem statement : 
# wap which accepts a file name from the user and count the total number of words in the file.
#
# Input :
# Marvellous.txt
#
# Expected output : 
# Total number of words in Demo.txt
#
######################################################################################################################

def main():
    try:
        TotalCount = 0

        fd = open("Marvellous.txt","r",encoding="cp1252")

        while True:
            line = fd.readline()

            if line == "":
                break

            if line == "\n":
                continue

            LineCount = 0

            for ch in line:
                if ch == " ":
                    LineCount += 1

            TotalCount += LineCount+1

        fd.close()

        print("Total number of words in Demo.txt : ",TotalCount)

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()