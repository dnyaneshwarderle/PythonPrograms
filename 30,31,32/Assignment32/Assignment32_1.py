import schedule
import time, datetime
def display():
    timestamp = time.ctime()
    print(timestamp)
    today = datetime.datetime.now()
    timestampFileName = "file_%s"%(timestamp)
    timestampFileName = timestampFileName.replace(" ","_")
    timestampFileName = timestampFileName.replace(":","_")

    fobj = open(f"AllFiles/{timestampFileName}.txt","w")
    fobj.write(f"File Name : {timestampFileName}.txt"+"\n")
    fobj.write(f"Creation date : {today.strftime("%d-%m-%Y")}"+"\n")
    fobj.write(f"Creation Time : {today.strftime("%d-%m-%Y")}"+"\n")
    fobj.close()

def main():
    schedule.every(1).minute.do(display)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()