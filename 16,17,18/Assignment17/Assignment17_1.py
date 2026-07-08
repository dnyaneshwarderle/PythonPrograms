from Arithmetic import *

def main():
    No1 = int(input("Enter 1st number: "))
    No2 = int(input("Enter 2nd number: "))

    print("---------------------Addition---------------------")
    ret = Add(No1,No2)
    print(f"Addition of {No1} and {No2} is :",ret)

    print("---------------------Substraction------------------")
    ret = Sub(No1,No2)
    print(f"Substraction of {No1} and {No2} is :",ret)

    print("---------------------Multiplication---------------")
    ret = Mult(No1,No2)
    print(f"Multiplication of {No1} and {No2} is :",ret)

    print("---------------------Division---------------------")
    ret = Div(No1,No2)
    print(f"Division of {No1} and {No2} is :",ret)


if __name__ == "__main__":
    main()