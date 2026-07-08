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
def main():
    No = int(input("Enter number: "))

    ret = ChkPrime(No)
    if ret == True:
        print("It is Prime number.")
    else:
        print("It is not prime number.")

if __name__ == "__main__":
    main()