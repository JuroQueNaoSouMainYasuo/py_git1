class Category():
    ledger = list()
    def deposit(self, amount, description=""):
        pass
    def withdraw(self, amount, description=""):
        pass
    def get_balance(self):
        pass
    def transfer(self, amount, category):
        pass
    def check_funds(self, amount):
        pass
    def __init__(self, name):
        self.name = name