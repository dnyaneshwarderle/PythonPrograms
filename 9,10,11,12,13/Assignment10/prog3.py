def Sum(val):
    result = 1
    for no in range(1,val+1):
        result = result * no
    return result

def main():
    no = int(input("Enter number: "))
    ret = Sum(no)
    print("Factorial is : ", ret)

if __name__ == "__main__":
    main()