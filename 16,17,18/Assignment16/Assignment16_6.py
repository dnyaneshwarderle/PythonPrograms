def ChkNo(No):
    if No == 0:
        return "Zero"
    elif No > 0:
        return True
    else:
        return False

def main():
    no = int(input("Enter Number to check: "))
    ret = ChkNo(no)
    if ret == "Zero":
        print("Zero")
    elif ret == True:
        print("Number is positive")
    else:
        print("Number is Negative")

if __name__ == "__main__":
    main()