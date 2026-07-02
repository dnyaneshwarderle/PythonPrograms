def ChkDiv(val):
    if (val % 3 == 0) and (val % 5 == 0):
        return True
    else:
        return False



def main():
    no = int(input("Enter number: "))
    ret = ChkDiv(no)
    if ret == True:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5.")


if __name__ == "__main__":
    main()