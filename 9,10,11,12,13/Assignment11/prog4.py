def Reverse(val):
    DigitStr = str(val)
    DigitLen = len(DigitStr)
    DigitStr1 = str()
    while DigitLen >= 1:
        DigitStr1 = DigitStr1 + DigitStr[DigitLen-1]
        DigitLen = DigitLen - 1

    return int(DigitStr1)

def Reverse1(val):
    DigitStr = str(val)
    return int(DigitStr[::-1])

def Reverse2(val):
    DigitStr = str(val)
    return int(''.join(reversed(DigitStr)))

def main():
    no = int(input("Enter number: "))
    ret = Reverse(no)
    print("Digit reverse number is: ", ret)

    ret1 = Reverse1(no)
    print("Digit reverse number using 2nd approche is: ", ret1)
   
    ret2 = Reverse2(no)
    print("Digit reverse number using 3nd approche is: ", ret2)

if __name__ == "__main__":
    main()