import multiprocessing
import os
import time

def Factor(No):
    print("Process is running with PID : ",os.getpid())
    fact = 1
    for i in range(1,No+1):
        fact += i ** 5
    print(f"Input number is: {No} and Factorial is: {fact}")
    return fact


def main():
    Data = [1000000,2000000,3000000,4000000]
    Result = list()
    start_time = time.time()
    
    pobj = multiprocessing.Pool()
    Result = pobj.map(Factor, Data)
    end_time = time.time()
    pobj.close()
    pobj.join()
    print(f"Execution time is : { end_time - start_time}")
    print("Result: ", Result)


if __name__ == "__main__":
    main()