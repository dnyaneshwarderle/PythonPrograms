from functools import reduce

def ChkPrime(No):
    fact = 0
    PrimeLst = list()
    if No == 2:
        return True
    for i in range(2,No):
        if No % i == 0:
            PrimeLst.append(i)
    if len(PrimeLst) == 0:
        return True
    else:
        return False

def CalMult(No):
    ret = No * 2
    return ret

def ChkMax(No1, No2):
    if No2 > No1:
        return No2

def main():
    No = int(input("Enter number of elements: "))
    InputLst = list()
    for i in range(No):
        InputLst.append(int(input(f"Enter Number: ")))
    ret =list(filter(ChkPrime,InputLst))
    print(f"List After filter {ret}")

    ret1 =list(map(CalMult,ret))
    print(f"List After Map {ret1}")

    ret2 =reduce(ChkMax,ret1)
    print(f"List After Reduce {ret2}")

if __name__ == "__main__":
    main()
    