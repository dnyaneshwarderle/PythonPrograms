def DigitSum(No):
    Digit = 0
    DigitStr = str(No)
    for val in DigitStr:
        Digit += int(val)

    return Digit

def main():
    No = int(input("Enter number: "))
    ret = DigitSum(No)
    print(f"Length of {No} is {ret}")

if __name__ == "__main__":
    main()