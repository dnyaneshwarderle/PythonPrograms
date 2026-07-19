def Table(val):
    MultTable = list()
    no = 1
    while no <= 10:
        if len(MultTable) == 0:
            MultTable.append(val)
        else:
            MultTable.append(val * no)
        no = no + 1
    return MultTable



def main():
    no = int(input("Enter number: "))
    ret = Table(no)
    for i in ret:
        print(i)


if __name__ == "__main__":
    main()