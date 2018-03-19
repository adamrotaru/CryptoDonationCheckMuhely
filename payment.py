# Represents a payment received

class Payment:
    def __init__(self, amount, currency, time, to_addr, from_addr, no_confirm):
        print("P", amount, currency, time, to_addr, from_addr, no_confirm)
        self.amount = amount
        self.currency = currency
        self.timestamp = time
        self.to_addr = to_addr
        self.from_addr = from_addr
        self.no_confirm = no_confirm

