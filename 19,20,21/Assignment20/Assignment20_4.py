import threading

def Small(val):
    small_thread = threading.current_thread()
    print("Thread ID of Small function is: ",small_thread.ident)
    print("Thread Name of Small function is: ",small_thread.name)
    SmallCnt = 0
    for char in val:
        if char.islower():
            SmallCnt += 1
    print("Small charactors are: ",SmallCnt)
    
def Capital(val):
    capital_thread = threading.current_thread()
    print("Thread ID of Capital function is: ",capital_thread.ident)
    print("Thread Name of Capital function is: ",capital_thread.name)
    CapCnt = 0
    for char in val:
        if char.isupper():
            CapCnt += 1
    print("Capital charactors are: ",CapCnt)

def Digit(val):
    digit_thread = threading.current_thread()
    print("Thread ID of Digit function is: ",digit_thread.ident)
    print("Thread Name of Digit function is: ",digit_thread.name)
    Digit = 0
    for char in val:
        if char.isdigit():
            Digit += 1
    print("Digits are: ",Digit)
    

def main():
    t1_obj = threading.Thread(target=Small, args=("Python",))
    t2_obj = threading.Thread(target=Capital, args=("Jay Ganesh",))
    t3_obj = threading.Thread(target=Digit, args=("Hellow 123 2",))

    t1_obj.start()
    t2_obj.start()
    t3_obj.start()

    t1_obj.join()    
    t2_obj.join()
    t3_obj.join()

    print("Exit from main.")

if __name__ == "__main__":
    main()