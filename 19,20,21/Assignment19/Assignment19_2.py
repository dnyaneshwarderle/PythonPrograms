PowerOfTwo = lambda x,y: x * y

def main():
    No1 = int(input("Enter 1st number: "))
    No2 = int(input("Enter 2nd number: "))
    ret = PowerOfTwo(No1, No2)
    print(f"Multiplication of {No1} and {No2} is ", ret)


if __name__ == "__main__":
    main()