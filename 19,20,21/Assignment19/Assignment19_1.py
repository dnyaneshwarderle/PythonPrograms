PowerOfTwo = lambda x: 2 ** x

def main():
    No = int(input("Enter a number: "))
    ret = PowerOfTwo(No)
    print(f"{No} Power of 2 is ", ret)


if __name__ == "__main__":
    main()