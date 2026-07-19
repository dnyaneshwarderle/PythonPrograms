def main():
    try:
        fileName = input("Enter the file name: ")

        fobj = open(fileName,"r")
        print("File gets opened")

        data = fobj.read()

        print(data)

        fobj.close()
    except FileNotFoundError as fobj:
        print("File is not present in current directory.")
    
if __name__ == "__main__":
    main()