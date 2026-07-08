def ListMin(InputLst):
    MinVal = InputLst[0]
    for val in InputLst:
        if MinVal > val:
            MinVal = val  
    return MinVal

def main():
    No = int(input("Enter number of elements: "))
    InputLst = list()
    for i in range(No):
        InputLst.append(int(input(f"Enter Number: ")))
    ret = ListMin(InputLst)
    print(f"Minimum from {InputLst} is {ret}")

if __name__ == "__main__":
    main()