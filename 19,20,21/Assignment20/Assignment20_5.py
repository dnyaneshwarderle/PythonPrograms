import threading

def Thread1():
    small_thread = threading.current_thread()
    print("Thread ID of Thread1 function is: ",small_thread.ident)
    print("Thread Name of Thread1 function is: ",small_thread.name)
    lst = list()
    print("1 to 50 numbers are: ")
    for val in range(1,51):
        lst.append(val)
    print(lst)
    
def Thread2():
    small_thread = threading.current_thread()
    print("Thread ID of Thread2 function is: ",small_thread.ident)
    print("Thread Name of Thread2 function is: ",small_thread.name)
    lst = list()
    print("50 to 1 numbers are: ")
    for val in range(50,0,-1):
        lst.append(val)
    print(lst)

    

def main():
    t1_obj = threading.Thread(target=Thread1)
    t1_obj.start()
    t1_obj.join()  

    t2_obj = threading.Thread(target=Thread2)
    t2_obj.start()
    t2_obj.join()

    print("Exit from main.")

if __name__ == "__main__":
    main()