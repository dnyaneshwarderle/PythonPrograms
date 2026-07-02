def Addition(val1, val2):
    result = val1 + val2
    return result

def Substraction(val1, val2):
    result = val1 - val2
    return result

def Multiplication(val1, val2):
    result = val1 * val2
    return result

def Division(val1, val2):
    result = val1 / val2
    return result
    
def main():
    no1 = int(input("Enter the 1st Number: "))
    no2 = int(input("Enter the 2nd Number: "))

    print("----------------Addition----------------")

    ret = Addition(no1, no2)
    print("Addition of ",no1," and ", no2, " is ", ret)

    print("----------------Substraction----------------")

    ret = Substraction(no1, no2)
    print("Substraction of ",no1," and ", no2, " is ", ret)

    print("----------------Multiplication----------------")

    ret = Multiplication(no1, no2)
    print("Multiplication of ",no1," and ", no2, " is ", ret)

    print("----------------Division----------------")

    ret = Division(no1, no2)
    print("Division of ",no1," and ", no2, " is ", ret)
   
if __name__ == "__main__":
    main()