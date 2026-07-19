import sys
def main():
    try:
        fileName1 = sys.argv[1]

        word = sys.argv[2]

        fobj = open(fileName1,"r")
        print("File gets opened")
        data = fobj.readlines()
        strCnt = 0
        for lines in data:
            cnt = lines.count(word)
            strCnt +=cnt
        print(f"{word} count into {fileName1} is {strCnt}")
        fobj.close()
    except FileNotFoundError as fobj:
        print("File is not present in current directory.")
    
if __name__ == "__main__":
    main()