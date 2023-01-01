class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = input(""" 
                 starting the procedure.....
                 1. Enter 1 to create your pin
                 2.Enter 2 to deposit money
                 3.Enter 3 to withdraw money
                 4.Enter 4 to check your balance 
                 5.Enter 5 to exit        
                           
                                 
                           
                           """)
        if user_input == "1":
          self.create_pin()
        elif user_input == "2":
          self.deposit()
        elif user_input == "3":
          self.withdraw()
        elif user_input == "4":
          self.check_balance()
        else :
           print("exit")
        
    def create_pin(self):
        self.pin = input("enter your pin: ")
        print("creating pin is successsful")
        self.menu()
        
    def deposit(self):
        temp=input("enter your pin: ")
        if temp==self.pin:
            amount=int(input("enter the amount to deposit: "))
            self.balance+=amount
            print("your balance is",self.balance)
        else:
            print("wrong pin")
            self.menu()
        
    def withdraw(self):
        temp=input("enter your pin: ")
        if temp==self.pin:
            amount=int(input("enter the amount to withdraw: "))
            if amount<self.balance:
                self.balance-=amount
                print("your balance is",self.balance)
            else:
                print("insufficient balance")
        else:
            print("wrong pin")
            self.menu()
            
    def check_balance(self):
        temp=input("enter your pin: ")
        if temp==self.pin:
            print("your balance is",self.balance)
        else:
            print("wrong pin")
            self.menu()
    
    
        
        
sbi=Atm()
sbi.create_pin()

sbi.deposit()
sbi.withdraw()
sbi.check_balance()


    



    