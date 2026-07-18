######################################################################################################################
#
# Frequency of string in a file
# 
# problem statement : 
# wap which accepts a file name and one string from the user and returns the frequency(count of occurences) of that 
# string in the file
#
# Input :
# Marvellous.txt    Marvellous
#
# Expected output : 
# Count how many times "Marvellous" appears in Marvellous.txt
#
######################################################################################################################
def main():
    try:
        FileName = input("Enter the file name: ")

        fd = open(FileName,"r",encoding="cp1252")

        word = input("Enter the word to search : ")

        ret = False

        Count = 0

        while True:

            line = fd.readline()

            if line == "":
                break

            if word in line:
                ret = True
                Count += 1

        fd.close()

        print("Frequency of the word",word,"in file",FileName,"is : ",Count)
       
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()