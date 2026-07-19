class BankAccount:
    ROI = 10.5
    def __init__(self,Name, Amount):
        self.Name = Name
        self.Amount = Amount
    
    def Display(self):
        print(f"Account Holder Name:{self.Name} \n Current balance: {self.Amount}")
    
    def Deposit(self):
        depositAmount = float(input("Enter amount to deposit: "))
        self.Amount += depositAmount
    
    def Withdraw(self):
        withdrawAmount = float(input("Enter amount to withdraw: "))
        self.Amount -= withdrawAmount
    
    def CalculateIntrest(self):
        Interest = (self.Amount * self.ROI) / 100
        self.Amount += Interest
        print(f"{Interest} Interest is deposited to you Account. ")
        print("Balance after adding interest: ",self.Amount)




obj1 = BankAccount("Dnyaneshwar", 100000)
obj1.Display()
obj1.Deposit()
obj1.Display()
obj1.Deposit()
obj1.Display()
obj1.Withdraw()
obj1.Display()
obj1.CalculateIntrest()
obj1.Display()
obj1.Withdraw()
obj1.Display()
obj1.CalculateIntrest()
obj1.Display()

