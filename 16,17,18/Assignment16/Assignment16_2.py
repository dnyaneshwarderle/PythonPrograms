def ChkNum(No):
    if No % 2 == 0:
        return True
    else:
        return False

def main():
    no = int(input("Enter the number: "))
    ret = ChkNum(no)
    if ret == True:
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()