def ChkGreater(val1,val2):
    if val1 > val2:
        return val1
    else:
        return val2


def main():
    no1 = 10
    no2 = 20
    ret = ChkGreater(no1,no2)
    print("Greater number is : ",ret)


if __name__ == "__main__":
    main()