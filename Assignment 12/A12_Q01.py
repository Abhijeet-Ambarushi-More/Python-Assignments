###########################################################
#
# WAP which accepts one character and checks whether it is 
# vowel or consonant
# 
# Input :  a
# Output : Vowel
#
###########################################################

def ChkVowel(ch):
    if((ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z')):
        if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
            return True
        else:
            return False
    else:
        print("Invalid character")


def main():
    Value = str(input("Enter the character : ")) 

    Ret = ChkVowel(Value)
    if (Ret == True):
        print("Vowel")
    elif(Ret == False):
        print("Consonant")

if __name__ == "__main__":
    main()