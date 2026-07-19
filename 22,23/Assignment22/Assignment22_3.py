import multiprocessing
import os

def ChkPrime(No):
    PrimeLst = list()
    PrimecntLst = list()
    for val in range(2,No):
        if val == 2:
            PrimecntLst.append(val)
        
        for i in range(2,val):
            if val % i == 0:
                PrimeLst.append(i)
        print(len(PrimeLst))
        if len(PrimeLst) == 0:
            
            PrimecntLst.append(val)
    return len(PrimecntLst)
        


def main():
    Data = [10000,20000,30000,40000]
    Result = list()

    pobj = multiprocessing.Pool()
    Result = pobj.map(ChkPrime, Data)

    pobj.close()
    pobj.join()

    print("Result: ", Result)


if __name__ == "__main__":
    main()