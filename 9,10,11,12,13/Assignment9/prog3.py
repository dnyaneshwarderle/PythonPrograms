def Square(val):
    CalSquare = val * val
    return CalSquare


def main():
    no = int(input("Enter number: "))
    ret = Square(no)
    print("Square of this number is: ",ret)


if __name__ == "__main__":
    main()