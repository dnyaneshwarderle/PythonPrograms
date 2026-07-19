def EvenNumber(val):
    EvenList = list()
    for no in range(1,val+1):
        if (no % 2 == 0):
            EvenList.append(no)
    return EvenList

def main():
    no = int(input("Enter number: "))
    ret = EvenNumber(no)
    print("Even numbers: ")
    for i in ret:
        print(i)

if __name__ == "__main__":
    main()