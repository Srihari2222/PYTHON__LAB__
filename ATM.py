# Write the following classes with class variables, instance variable and
# illustration the self variable
#           1 (ii). ATM (to deposit and withdraw amount from ATM machine)
class ATM:
    def __init__(self):
        self.amount = 50000

    def w(self):
        withdraw = int(input("Enter the amount to withdraw: "))
        if self.amount < withdraw:
            print(f"Insufficient balance")
        else:
            self.amount = self.amount - withdraw
            print(f"Remaining balance: {self.amount}")

    def d(self):
        deposit = int(input("Enter the amount to deposit: "))
        self.amount = self.amount + deposit
        print(f"Updated balance: {self.amount}")


atm = ATM()
atm.w()
atm.d()