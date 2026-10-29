from abc import ABC, abstractmethod

'''
Deine Aufgabe

1. Schreibe die Klasse StripeAdapter. Sie soll PaymentProvider implementieren und intern StripeSDK benutzen.

2. Baue Checkout mit deinem Adapter zusammen und rufe finish(49.99) auf.
'''

# Der Standard, den dein Code erwartet
class PaymentProvider(ABC):
    @abstractmethod
    def pay(self, amount):
        ...

# Dein Code: kennt nur den Standard
class Checkout:
    def __init__(self, provider):
        self.provider = provider

    def finish(self, amount):
        self.provider.pay(amount)

# Fremder Code: darfst du nicht ändern
class StripeSDK:
    def charge(self, amount):
        print(f"Stripe: {amount} abgebucht")

class StripeAdapter(PaymentProvider):
    def __init__(self):
        self.sdk = StripeSDK()

    def pay(self, amount):
        self.sdk.charge(amount)


checkout = Checkout(StripeAdapter())
checkout.finish(49.99)
