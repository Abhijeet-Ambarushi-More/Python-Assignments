######################################################################################################################
#
# Search a word in a file
# 
# problem statement : 
# wap which accepts a file name and a word from the user and checks whether that word is present in the file or not
#
# Input :
# Marvellous.txt    Marvellous
#
# Expected output : 
# Display whether the word Marvellous is found in Marvellous.txt or not 
#
######################################################################################################################
def main():
    try:
        fd = open("Marvellous.txt", "r",encoding="cp1252")

        word = input("Enter the word to search : ")

        ret = False

        while True:

            line = fd.readline()

            if line == "":
                break

            if word in line:
                ret = True
                break

        fd.close()

        if ret:
            print(word, "is present in the file Marvellous.txt")
        else:
            print(word, "is not present in the file Marvellous.txt")
       
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()