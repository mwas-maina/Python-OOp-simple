class Bank():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,add):
        self.balance=self.balance +add
        return self.balance
    def ret(self):
        return f"You have deposited {user}.New balance is {account.deposit(user)}"
        
        
    def withdraw(self,withdraw):
        self.balance=self.balance-withdraw
        if self.balance< withdraw:
            print("Your Account balance is less than the required amount")
            
        else:
            return "You have withdrawan {}.Your account balance is Ksh {}".format(withdraw,self.balance)  
        
    def __str__(self):
        return f" account name: {self.owner} \n balance: ${self.balance}" 
    
    
account=Bank("emmanuel",5000)

user=input("Please enter your Pin to proceed   ")
if user !="1999" :
    print("Enter a valid Pin.exiting....")
else:
    print("Welcome Emmanuel to Kcb Account no 1213571928\n") 
user=input("Please check your balance .Reply with 1 ") 
if user !="1" :
    print("Enter a valid number.exiting....")
else:
    
    print(f"Your balance is {account.balance}")
    
user=int(input("Please enter Amount to Deposit "))
print(account.ret())
#withdraw
widthdraw_input=eval(input('Please enter the amount to withdraw'))
balance_after_withdrawer=account.withdraw(widthdraw_input)
print(balance_after_withdrawer)
print(str(account))





    
      

     
        
        
        
    
        
       
    
 