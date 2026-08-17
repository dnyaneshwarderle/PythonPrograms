import schedule
import time, datetime
def display():
    timestamp = time.ctime()
    timestampFileName = "Data_%s"%(timestamp)
    timestampFileName = timestampFileName.replace(" ","_")
    timestampFileName = timestampFileName.replace(":","_")
    fobj = open("backup_log.txt","r")
    fobj1 = open("Backup/"+timestampFileName+".txt","w")
    data = fobj.read()
    fobj1.write(data+"\n")
    fobj1.close()
    fobj.close()

def main():
    schedule.every(60).minutes.do(display)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()