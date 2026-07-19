def CheckDigit(val):
    DigitStr = str(val)
    DigitCount = len(DigitStr)
    return DigitCount

def main():
    no = int(input("Enter number: "))
    ret = CheckDigit(no)
    print("Digit count is: ", ret)
   

if __name__ == "__main__":
    main()