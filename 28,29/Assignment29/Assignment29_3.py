import sys
def main():
    try:
        fileName1 = sys.argv[1]

        fileName2 = sys.argv[2]

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