
def main():
    try:
        fileName1 = input("Enter the 1st file name: ")

        fileName2 = input("Enter the 2nd file name: ")

        fobj1 = open(fileName1,"r")
        print("File gets opened")
        fobj2 = open(fileName2,"w")
        data = fobj1.readlines()
        for lines in data:
            fobj2.write(lines)

        
        fobj2.close()
        fobj1.close()
    except FileNotFoundError as fobj:
        print("File is not present in current directory.")
    
if __name__ == "__main__":
    main()