import MarvellousNum

def ListPrime(InputLst):
    PrimeCnt = 0
    for val in InputLst:
        ret = MarvellousNum.ChkPrime(val)
        if ret == True:
            print(val)
            PrimeCnt +=val
    return PrimeCnt

def main():
    No = int(input("Enter number of elements: "))
    InputLst = list()
    for i in range(No):
        InputLst.append(int(input(f"Enter Number: ")))
    ret = ListPrime(InputLst)
    print(f"Addition of all prime number from {InputLst} is {ret}")

if __name__ == "__main__":
    main()

#[13, 5, 45, 7, 4, 56, 10, 34, 2, 5, 8]