def ChkDiv(val):
    CalCube = val * val * val
    return CalCube


def main():
    no = int(input("Enter number: "))
    ret = ChkDiv(no)
    print("Divisible by 3 and 5 : ",ret)


if __name__ == "__main__":
    main()