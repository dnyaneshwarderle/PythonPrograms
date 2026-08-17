import schedule
import time, datetime
def display():
    timestamp = time.ctime()
    print(timestamp)
    today = datetime.datetime.now()
    timestampFileName = "file_%s"%(timestamp)
    timestampFileName = timestampFileName.replace(" ","_")
    timestampFileName = timestampFileName.replace(":","_")
    FileName = "FileSizeLog.txt"
    fobj = open(FileName,"w")
    fobj.write(f"File Name : {timestampFileName}.txt"+"\n")
    fobj.write(f"Creation date : {today.strftime("%d-%m-%Y")}"+"\n")
    fobj.write(f"Creation Time : {today.strftime("%d-%m-%Y")}"+"\n")
    fobj.close()

def main():
    schedule.every(30).seconds.do(display)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()