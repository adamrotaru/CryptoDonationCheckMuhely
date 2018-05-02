# Represents a payment check result, multiple currencies

import payment

import datetime

class PaymentResultMulti:
    def __init__(self, time_from, time_to, payments):
        self.time_from = time_from
        self.time_to = time_to
        self.payments = payments

    def print(self):
        if len(self.payments) == 0:
            print("There are no new payments :(", end="")
        else:
            if len(self.payments) == 1:
                print("There is one new payment.", end="")
            else:
                print("There are", len(self.payments), "new payments.", end="")
        print("  period:", datetime.datetime.fromtimestamp(self.time_from).__str__(), "-", datetime.datetime.fromtimestamp(self.time_to).__str__() + " UTC")
        for p in self.payments:
            print("-", p.to_string())

    def count(self):
        return len(self.payments)

    def add(self, amount, currency, time, to_addr, from_addr, no_confirm):
        self.payments.append(payment.Payment(amount, currency, time, to_addr, from_addr, no_confirm))
        
        
