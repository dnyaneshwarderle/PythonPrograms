import schedule,sys
import time, datetime,os

def DirectoryScanner(DirectoryPath):
    subCount = 0
    fileCount = 0
    for folderName, subFolder, fileName in os.walk(DirectoryPath):
        print("Directory name: ",folderName)
        
        for subF in subFolder:
            subCount+=1
        for fileN in fileName:
            fileCount+=1
    print("Total Files: ",subCount)
    print("Total Sub Directories",fileCount)
    print("Scan Time:" , time.ctime())

def main():
    dirName = str(input("Enter Directory name:"))
    schedule.every(1).minute.do(DirectoryScanner, dirName)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()