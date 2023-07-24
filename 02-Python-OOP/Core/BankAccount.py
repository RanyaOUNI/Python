
class BankAccount :

# ! <----------CONSTRUCTOR --------------->

   def __init__(self,int_rate,balance):
        self.balance = balance
        self.int_rate = int_rate


# !  DEPOSIT METHOD 

   def deposit(self,amount):
      self.balance += amount
      print(f"The amount is : {amount} $")


# !  WITHDROW METHODS 

def withdrow(self,amount):
   if amount < self.balance :
      self.balance -= amount
   else:
      print(f"Insufficient funds: Charging a $5 fee")
      self.balance -= 5

# ! DISPLAY_ACCOUNT_INFO METHOD 

   def display_info(self,):
      print(f"Balance: {self.balance}")

# ! YIELD_INTEREST 

   def yield_interest(self):
      if self.balance > 0:
         self.balance = self.balance*self.int_rate


# ! INSTANCIATION 

account1 = BankAccount(0.17,700)
account2 = BankAccount(0.3,1000)

# account1.deposit(50)
# account1.deposit(100)

account1.deposit(50).deposit(100).deposit(200).withdraw(300).yield_interest().display_account_info()




