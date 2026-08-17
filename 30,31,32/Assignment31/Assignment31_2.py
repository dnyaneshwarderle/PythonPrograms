import schedule,sys
import time, datetime
def DisplayMessage(message):
    print(message)

def main():
    message = str(input("Enter Message:"))
    schedule.every(5).seconds.do(DisplayMessage, message)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()