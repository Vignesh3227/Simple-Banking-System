class BankAccount:
    total_accounts=0
    def __init__(self, owner,balance):
        self.owner=owner
        self.__balance=balance
        BankAccount.total_accounts+=1
    
    def deposit(self,amt):
        if amt>0:
            self.__balance=self.__balance + amt
            return True
        else:
            return False
        
    def withdraw(self,amt):
        if amt>0 and self.__balance>=amt:
            self.__balance=self.__balance-amt
            return True
        else:
            return False
    @property 
    def balance(self):
        return self.__balance
    @balance.setter 
    def balance(self,balance):
        if balance>=0:
            self.__balance=balance

    def __str__(self):
        return f"Your account name: {self.owner}\n Remaining Balance: {self.__balance}"
    
    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.__balance})"

    def __add__(self,other):
        new_owner=self.owner+"and"+other.owner
        new_balance=self.__balance+other.__balance
        return BankAccount(new_owner,new_balance)
    
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate=0.05):
        super().__init__(owner,balance)
        self.interest_rate=interest_rate
    
    def apply_interest(self):
        self.deposit(self.balance*self.interest_rate)
    
class CheckingAccount(BankAccount):
    def __init__(self, owner, balance,overdraft_limit=0):
        super().__init__(owner, balance)
        self._overdraft_limit=overdraft_limit
    
    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self,val):
        if val>=0:
            self._overdraft_limit=val

    def withdraw(self, amt):
        if amt> 0 and (self.balance+self._overdraft_limit)>=amt:
            self._BankAccount__balance -= amt
            return True
        else:
            return False

class Customer:
    def __init__(self,name):
        self.name=name
        self.accounts=[]
    
    def add_account(self, account):
        self.accounts.append(account)


    def total_balance(self):
        return sum(acc.balance for acc in self.accounts)

    def transfer(self, from_acc, to_acc, amt):
        if from_acc.withdraw(amt):
            to_acc.deposit(amt)
            return True
        else:
            return False   
        
def print_account_summary(obj):
    print(f"owner: {obj.owner}, balance: {obj.balance}")
