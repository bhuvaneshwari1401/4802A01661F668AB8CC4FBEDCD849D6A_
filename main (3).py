class BankAccount:
    def_init_(self,account_number,account_holder_name,initial_balance=0.0):
    self_account_number=self_account_number
  
    self_account_holder_name=account_holder_name
      self_account_balance=initial_balance

def deposit(self,amount):
  if amount>0:
    self_account_balance+=amount
    print(f"Deposited$ {amount:.2f}into account{self_account_number}")
  else:
    print("Invalid deposit amount.Please deposit a positive amount.")

def withdraw(self,amount):
  if amount>0:
    if
    self_account_balance>=amount:

self_account_balance-=amount
print(f"Withdrew ${amount:.2f}from account {self_account_number}")
else:
print("Invalid withdrawal amount.Please withdraw a positive amount.")

def display_balance(self):
  print(f"Account{self_account_number}balance:$
  {self_account_balance:.2f}")

#Testing the BankAccount class if name=="_main_":
#create a BankAccount instanceaccount1=BankAccount("123456","John Doe",1000.0)

#deposit money account1.deposit(500.0)

#withdraw money account1.withdraw(200.0)

#Display balance account1.display_balance()