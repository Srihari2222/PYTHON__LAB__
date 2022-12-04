class ATM:
    amount=50000

    def deposit(self):
        dep_amount=int(input("Enter the amount to be deposited: "))
        ATM.amount=ATM.amount+dep_amount
        print(f"Updated Amount is: {ATM.amount}")
    def withdraw(self):
        wit_amount=int(input("Enter the amount to be withdrawn: "))
        if wit_amount>ATM.amount:
            print("Insufficient balance!!")
        else:
            ATM.amount-=wit_amount
            print(f"Remaining balance: {ATM.amount}")

print(ATM.__dict__)
ATM().withdraw()
ATM().deposit()