######################################################################################################################
#
# Count words in a file
# 
# problem statement : 
# wap which accepts a file name from the user and displays the contents of the file line by line on the screen
#
# Input :
# Marvellous.txt
#
# Expected output : 
# Display each line of Marvellous.txt one by one
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

            print(line)

        fd.close()
       
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()