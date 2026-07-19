import os
import sys

def main():
    fileName = sys.argv[1]

    if os.path.isfile(fileName):
        print("File is exists into current directory")
    else:
        print("File is not exists in current directory.")

if __name__ == "__main__":
    main()