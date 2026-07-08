from functools import reduce

def ChkEven(No):
    if No % 2 == 0:
        return True

def CalSquar(No):
    ret = No ** 2
    return ret

def Addition(No1,No2):
    ret = No1 + No2
    return ret

def main():
    No = int(input("Enter number of elements: "))
    InputLst = list()
    for i in range(No):
        InputLst.append(int(input(f"Enter Number: ")))
    ret =list(filter(ChkEven,InputLst))
    print(f"List After filter {ret}")

    ret1 =list(map(CalSquar,ret))
    print(f"List After Map {ret1}")

    ret2 =reduce(Addition,ret1)
    print(f"List After Reduce {ret2}")

if __name__ == "__main__":
    main()
    