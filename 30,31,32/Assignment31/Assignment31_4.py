import schedule
import time, datetime
def Logs():
    timestamp = time.ctime()
    timestampFileName = "Data_%s"%(timestamp)
    timestampFileName = timestampFileName.replace(" ","_")
    timestampFileName = timestampFileName.replace(":","_")
    fobj1 = open("Logs/"+timestampFileName+".txt","w")
    
    fobj1.write("Log File created successfully."+"\n")
    fobj1.write(f"creation time is {time.ctime()}"+"\n")
    fobj1.close()

def main():
    schedule.every(10).minutes.do(Logs)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()