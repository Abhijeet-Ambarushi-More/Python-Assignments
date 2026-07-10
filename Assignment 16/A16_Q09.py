###########################################################
#
# WAP which display first 10 even numbers on screen
#
###########################################################

def DisplayFirst10Even():
    for i in range(1,11):
        print(i*2, end = "  ")

def main():
   DisplayFirst10Even()

if __name__ == "__main__":
    main()