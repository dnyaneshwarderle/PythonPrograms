def ChkNum(No):
    if No % 2 == 0:
        return No

def main():
    no = 1
    EvenList = list()
    while len(EvenList) != 10:
        if no % 2 == 0:
            EvenList.append(no)
            print(no)
        no +=1
    print(EvenList)
if __name__ == "__main__":
    main()