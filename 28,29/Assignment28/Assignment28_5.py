
def main():
    try:
        fileName = input("Enter the file name: ")
        word = input("Enter the Word to search: ")
        fobj = open(fileName,"r")
        print("File gets opened")

        data = fobj.read()
        if word in data:
            print(f"{word} is present in {fileName}")
        else:
            print(f"Word not present in {fileName}")

        
        fobj.close()
    except FileNotFoundError as fobj:
        print("File is not present in current directory.")
    
if __name__ == "__main__":
    main()