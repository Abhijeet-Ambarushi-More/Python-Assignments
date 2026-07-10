###########################################################
#
# WAP which accepts name from user and display length of
# its name
#
# Input : Marvellous    Output : 10
#
###########################################################

def DisplayLenth(Str):
    print(len(Str))

def main():
   Name = input("Enter the name : ")
   DisplayLenth(Name)

if __name__ == "__main__":
    main()