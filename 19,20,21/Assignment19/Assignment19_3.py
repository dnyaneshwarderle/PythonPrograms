from functools import reduce

ChkNum = lambda x: x >= 70 and x <= 90
IncreaseNum = lambda x: x + 10
ProdNum = lambda x, y: x * y

def main():
    No = int(input("Enter number of elements: "))
    InputLst = list()
    for i in range(No):
        InputLst.append(int(input(f"Enter Number: ")))
    ret =list(filter(ChkNum,InputLst))
    print(f"List After filter {ret}")

    ret1 =list(map(IncreaseNum,ret))
    print(f"List After Map {ret1}")

    ret2 =reduce(ProdNum,ret1)
    print(f"List After Reduce {ret2}")

if __name__ == "__main__":
    main()
    