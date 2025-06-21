from banking import BankAccount, SavingsAccount, CheckingAccount, Customer, print_account_summary

acc1= BankAccount("Vignesh",1000)
acc2= BankAccount("Satyaki", 5000)
acc1.deposit(100)
acc1.deposit(200)
merged=acc1+acc2

savings=SavingsAccount("Mohit",1000,0.05)
checking=CheckingAccount("Mrutyunjay",5000,200)
savings.apply_interest()
checking.withdraw(650)

cust=Customer("Balaji")
cust.add_account(savings)
cust.add_account(checking)
cust.transfer(savings,checking,100)

for acc in [acc1, acc2, merged, savings, checking]:
    print_account_summary(acc)
    print(repr(acc))

print(f"Total balance of {cust.name}: {cust.total_balance():.2f}")