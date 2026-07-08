import threading

def CalSum(No, Result):
    total = sum(No)
    Result["sum"] = total


def CalProd(No, Result):
    prod = 1

    for num in No:
        prod *= num

    Result["product"] = prod

    
def main():
    NoList = [1, 2, 3, 4, 5]
    Result = dict()
    t1_obj = threading.Thread(target=CalSum, args=(NoList, Result))
    t2_obj = threading.Thread(target=CalProd, args=(NoList, Result))

    t1_obj.start()
    t2_obj.start()

    t1_obj.join()  
    t2_obj.join()

    print(f"Sum of the {NoList} is ", Result['sum'])
    print(f"product of the {NoList} is ", Result['product'])

    print("Exit from main.")

if __name__ == "__main__":
    main()