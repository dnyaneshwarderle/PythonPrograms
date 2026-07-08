import threading

def EvenNum():
    EvenList = list()
    cnt = 1
    while len(EvenList) != 10:
        if cnt % 2 == 0:
            EvenList.append(cnt)
        cnt+=1
    print(EvenList)
    
def OddNum():
    OddList = list()
    cnt = 1
    while len(OddList) != 10:
        if cnt % 2 != 0:
            OddList.append(cnt)
        cnt+=1
    print(OddList)
    

def main():
    print("First 10 Even number list is: ", end=" ")
    t1_obj = threading.Thread(target=EvenNum)
    t1_obj.start()
    t1_obj.join()

    print("First 10 Odd number list is: ", end=" ")
    t2_obj = threading.Thread(target=OddNum)
    t2_obj.start()
    t2_obj.join()



if __name__ == "__main__":
    main()