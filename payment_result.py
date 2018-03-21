# Represents a payment check result

import payment

class PaymentResult:
    def __init__(self, time_from, time_to, payments):
        self.time_from = time_from
        self.time_to = time_to
        self.payments = payments

    def print(self):
        if len(self.payments) == 0:
            print("There are no new payments :(")
            return
        if len(self.payments) == 1:
            print("There is one new payment!")
        else:
            print("There are", len(self.payments), "new payments!")
        for p in self.payments:
            print("-", p.to_string())
        print("Check included period:", self.time_from, "-", self.time_to)

    def count(self):
        return len(self.payments)
        
