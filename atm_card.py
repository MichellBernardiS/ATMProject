class AtmCard:
    def __init__(self, defaultPin, defaultBalance):
        self.card_pin = defaultPin
        self.card_balance = defaultBalance

    def get_defaultbalance(self):
        return self.card_balance
    
    def get_defaultpin(self, card_pin):
        return self.card_pin