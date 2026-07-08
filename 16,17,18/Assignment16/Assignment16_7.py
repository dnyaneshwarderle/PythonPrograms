def ChkNum(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():
    no = int(input("Enter the number: "))
    ret = ChkNum(no)
    print(ret)

if __name__ == "__main__":
    main()