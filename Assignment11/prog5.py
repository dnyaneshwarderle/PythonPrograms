def CheckPalindrome(val):
    DigitStr = str(val)
    DigitLen = len(DigitStr)
    DigitStr1 = str()
    while DigitLen >= 1:
        DigitStr1 = DigitStr1 + DigitStr[DigitLen-1]
        DigitLen = DigitLen - 1

    return int(DigitStr1) == val

def CheckPalindrome1(val):
    DigitStr = str(val)
    return int(DigitStr[::-1]) == val

def CheckPalindrome2(val):
    DigitStr = str(val)
    return int(''.join(reversed(DigitStr))) == val

def main():
    no = int(input("Enter number: "))
    ret = CheckPalindrome(no)
    print("------------------First Approche------------------")
    print("Check Number is palindrome or not using 1st Approche")
    if ret == True:
        print("This number is palindrome")
    else:
        print("This number is not palindrome.")

    print("------------------Second Approche------------------")

    ret = CheckPalindrome1(no)
    print("Check Number is palindrome or not using 2nd Approche")
    if ret == True:
        print("This number is palindrome")
    else:
        print("This number is not palindrome.")

    print("------------------Third Approche------------------")    

    ret = CheckPalindrome2(no)
    print("Check Number is palindrome or not using 3rd Approche")
    if ret == True:
        print("This number is palindrome")
    else:
        print("This number is not palindrome.")


if __name__ == "__main__":
    main()