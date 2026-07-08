def DigitLen(No):
    return len(str(No))
def main():
    No = int(input("Enter number: "))
    ret = DigitLen(No)
    print(f"Length of {No} is {ret}")

if __name__ == "__main__":
    main()