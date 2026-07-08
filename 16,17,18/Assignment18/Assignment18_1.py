def ListSum(InputLst):
    Digit = 0
    for val in InputLst:
        Digit += val
    return Digit

def main():
    No = int(input("Enter number of elements: "))
    InputLst = list()
    for i in range(No):
        InputLst.append(int(input(f"Enter Number: ")))
    ret = ListSum(InputLst)
    print(f"Length of {No} is {ret}")

if __name__ == "__main__":
    main()