import multiprocessing
import os
import time

def SumOdd(No):
    print("Process is running with PID : ",os.getpid())
    sumOdd = 0
    for i in range(1,No+1):
        if i % 2 != 0:
            sumOdd += 1 
    print(f"Input number is: {No} and Sum of even is: {sumOdd}")
    return sumOdd


def main():
    Data = [1000000,2000000,3000000,4000000]
    Result = list()
    start_time = time.time()
    
    pobj = multiprocessing.Pool()
    Result = pobj.map(SumOdd, Data)
    end_time = time.time()
    pobj.close()
    pobj.join()
    print(f"Execution time is : { end_time - start_time}")
    print("Result: ", Result)


if __name__ == "__main__":
    main()