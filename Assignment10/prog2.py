def Sum(val):
    MultTable = list()
    result = 0
    for no in range(val+1):
        result = result + no
    return result

def main():
    no = int(input("Enter number: "))
    ret = Sum(no)
    print("Sum of Natural numbers is : ", ret)

if __name__ == "__main__":
    main()