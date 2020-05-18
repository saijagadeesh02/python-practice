class Account:
    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance

    def deposit(self,value):
        self.balance = self.balance + value

    def withdrawl(self,val):
        if val<=self.balance:
            self.balance = self.balance - val
            print(f"You just withdrawed {val} and your current balance is {self.balance}")
        else:
            print("Unavailable funds")

    def __str__(self):
        return f'{self.owner} current balance is {self.balance}'

c1 = Account('Jose',100)
c2 = Account('Sarah',1500)
c1.deposit(2000)
c1.deposit(2000)
c2.withdrawl(3000)
print(c1)
print(c2)

