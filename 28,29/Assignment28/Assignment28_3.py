
def main():
    try:
        fileName = input("Enter the file name: ")

        fobj = open(fileName,"r")
        print("File gets opened")

        data = fobj.readlines()
        for lines in data:
            print(lines)

        
        fobj.close()
    except FileNotFoundError as fobj:
        print("File is not present in current directory.")
    
if __name__ == "__main__":
    main()