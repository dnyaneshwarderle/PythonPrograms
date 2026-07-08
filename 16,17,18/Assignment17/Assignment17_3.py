def Factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact *=i

    return fact

def main():
    No = int(input("Enter number: "))

    ret = Factorial(No)
    print(f"Factiorial of {No} is {ret}")

if __name__ == "__main__":
    main()