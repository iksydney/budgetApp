print("Green Budget")
class Budget:
    def __init__(self, food, clothing, entertainment): 
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        
    def balance(self):
        self.balance = 0
        
    def deposit(self):
        amount = double(input("Enter te amount to be deposited"))
        self.balance = self.balance + amount
        print("The deposit is successful and the balance of the category is %f" % self.balance)
        
    def withdraw(self):
        amount = double(input("Enter the amont you would like to withdraw \n"))
        if (self.balance >= amount):
            self.balance =self.balance - amount
            print("The withdrawal is successful %f" % self.balance)
        else:
            print("Insufficient balance %")
    
    def enquiry(self):
        print("Balance in the account is %f" % self.balance)
    
    print("""Select a category
          1 == Foood
          2 == Clothing
          3 == Entertainment
          4 == exit
          """)
            option = int(input("please enter your choice"))
        
