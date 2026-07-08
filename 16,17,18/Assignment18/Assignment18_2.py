def ListMax(InputLst):
    MaxVal = 0
    for val in InputLst:
        if MaxVal < val:
            MaxVal = val  
    return MaxVal

def main():
    No = int(input("Enter number of elements: "))
    InputLst = list()
    for i in range(No):
        InputLst.append(int(input(f"Enter Number: ")))
    ret = ListMax(InputLst)
    print(f"Maximim from {InputLst} is {ret}")

if __name__ == "__main__":
    main()