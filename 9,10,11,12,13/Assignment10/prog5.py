def OddNumber(val):
    OddList = list()
    for no in range(1,val+1):
        if (no % 2 != 0):
            OddList.append(no)
    return OddList

def main():
    no = int(input("Enter number: "))
    ret = OddNumber(no)
    print("Odd numbers: ")
    for i in ret:
        print(i)

if __name__ == "__main__":
    main()