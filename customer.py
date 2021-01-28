from atm_card import AtmCard

class Customer:
    def __init__(self, id, custPin = 1234, custBalance = 10000):
        self.custid = id
        self.custPin = custPin
        self.custBalance = custBalance
    
    def get_customer_id(self):
        return self.custid
    
    def get_customer_pin(self):
        return self.custPin
    
    def get_customer_balance(self):
        return self.custBalance

    def debit(self, nominal):
        self.custBalance -= nominal

    def credit(self, nominal):
        self.custBalance += nominal