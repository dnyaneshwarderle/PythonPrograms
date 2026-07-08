def FactorSum(No):
    fact = 0
    for i in range(1,No):
        if No % i == 0:
            fact +=i

    return fact

def main():
    No = int(input("Enter number: "))

    ret = FactorSum(No)
    print(f"Factior Addition of {No} is {ret}")

if __name__ == "__main__":
    main()