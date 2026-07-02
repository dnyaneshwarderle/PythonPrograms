def CheckDigit(val):
    DigitStr = str(val)
    DigitList = list(DigitStr)
    DigitCount = len(DigitList)
    return DigitCount

def main():
    no = int(input("Enter number: "))
    ret = CheckDigit(no)
    print("Digit Sum is: ", ret)
   

if __name__ == "__main__":
    main()