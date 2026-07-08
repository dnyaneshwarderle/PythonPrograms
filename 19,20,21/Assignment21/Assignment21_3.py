import threading
    
cnt = 0
lock = threading.Lock()

def IncrementCnt(times):
    global cnt

    for _ in range(times):
        with lock:
            cnt += 1

def main():
    threads = []
    NumThreads = 5
    IncrementTimes = 1000

    for i in range(NumThreads):
        t = threading.Thread(target=IncrementCnt, args=(IncrementTimes,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print(cnt)
    print("Exit from main.")

if __name__ == "__main__":
    main()