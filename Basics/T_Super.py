class monAcount:
    def __init__(self, years, payment):
        self.years = years
        self.payment = payment
    def checkBalance(self):
        print('Mon balance: ')
        print('Giving age: ', self.years)

class dadAcount:
    def __init__(self, name, balance):
        self.name = name
        self.balace = balance
    def checkBalance(self):
        print('the Balance is: ', self.balace)

class childAcount(dadAcount, monAcount):
    def __init__(self, name, balance, is_child = True):
        super().__init__(name, balance)
        self.is_child = is_child
    def checkBalance(self):
        print('This is a child Account')
        super().checkBalance()    
anton = childAcount('Anton', 2000)
anton.checkBalance()    