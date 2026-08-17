import schedule,sys
import time, datetime
def display(message):
    print(message)

def main():
    message = str(input("Enter Message:"))
    timeInterval = float(input("Enter Interval in seconds:"))
    schedule.every(timeInterval).seconds.do(display, message)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()