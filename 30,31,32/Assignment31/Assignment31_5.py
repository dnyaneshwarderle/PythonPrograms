import schedule,sys
import time, datetime,os

def DirectoryScanner(DirectoryPath):
    subCount = 0
    fileCount = 0
    fobj1 = open("Logs/"+timestampFileName+".txt","w")
    
    for folderName, subFolder, fileName in os.walk(DirectoryPath):
        fobj1.write(f"Directory name: {folderName}"+"\n")
        for subF in subFolder:
            subCount+=1
        for fileN in fileName:
            fileCount+=1
    
    fobj1.write(f"Total Files: {subCount}"+"\n")
    fobj1.write(f"Scan Time: {time.ctime()}"+"\n")
    
    fobj1.close()

def main():
    dirName = str(input("Enter Directory name:"))
    schedule.every(5).minutes.do(DirectoryScanner, dirName)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()