import multiprocessing

def SumNum(No):
    Sum = 0

    for i in range(No):
        Sum += i**2
    return Sum

def main():
    Data = [1000000,2000000,3000000,4000000]
    Result = list()

    pobj = multiprocessing.Pool()
    Result = pobj.map(SumNum, Data)

    pobj.close()
    pobj.join()

    print("Result: ", Result)


if __name__ == "__main__":
    main()