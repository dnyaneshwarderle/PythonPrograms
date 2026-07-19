import multiprocessing
import os
import time

def Factorial(No):
    print("Process is running with PID : ",os.getpid())
    fact = 1
    for i in range(1,No+1):
        fact *=i
    print(f"Input number is: {No} and Factorial is: {fact}")
    return fact



def main():
    Data = [10,15,20,25]
    Result = list()
    start_time = time.time()
    
    pobj = multiprocessing.Pool()
    Result = pobj.map(Factorial, Data)
    end_time = time.time()
    pobj.close()
    pobj.join()
    print(f"Execution time is : { end_time - start_time}")
    print("Result: ", Result)


if __name__ == "__main__":
    main()