def main():
    try:
        fileName = input("Enter the file name: ")

        fobj = open(fileName,"r")
        print("File gets opened")

        data = fobj.readlines()
        wordCnt = 0
        for lines in data:
            wordLst = lines.split(" ")
            wordCnt += len(wordLst)

        print(f"Total number of words in {fileName} are {wordCnt}")
        
        fobj.close()
    except FileNotFoundError as fobj:
        print("File is not present in current directory.")
    
if __name__ == "__main__":
    main()