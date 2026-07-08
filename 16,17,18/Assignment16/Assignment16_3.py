def Add(No1, No2):
    result = No1 + No2
    return result

def main():
    no1 = int(input("Enter the 1st number: "))
    no2 = int(input("Enter the 2nd number: "))
    ret = Add(no1, no2)
    print(f"Addition of {no1} and {no2} is: ", ret)

if __name__ == "__main__":
    main()