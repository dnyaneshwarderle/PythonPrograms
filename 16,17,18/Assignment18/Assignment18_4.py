def ChkFreq(InputLst,No):
    cnt = 0
    for val in InputLst:
        if val == No:
            cnt +=1
    return cnt

def main():
    No = int(input("Enter number of elements: "))
    InputLst = list()
    for i in range(No):
        InputLst.append(int(input(f"Enter Number: ")))
    No1 = int(input("Enter number to check frequency: "))
    ret = ChkFreq(InputLst, No1)
    print(f"Frequency of {No1} in {InputLst} is {ret}")

if __name__ == "__main__":
    main()