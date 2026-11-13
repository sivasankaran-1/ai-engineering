class Customer:
    def greet(self):
        print("Hello")

customer1 = Customer()
customer2 = Customer()
customer3 = Customer()
customer1.greet()

customer2.greet()

customer3.greet()

#Constructor and self

#What is __init__(). __init__ is a special initialization method.

class Customer():
    def __init__(self, age, name):
        self.name = name
        self.age = age


customer1 = Customer("Arun", 28)
customer2 = Customer("Priya", 25)


print(customer1.name)
print(customer1.age)

print(customer2.name)
print(customer2.age)

#Attributes and methods

class Customer:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance


customer1 = Customer("Arun", 5000)
customer2 = Customer("Priya", 10000)


print(customer1.balance)
print(customer2.balance)


#Instance methods

class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

    def show_balance(self):

        print(self.balance)
    
    def withdraw(self, amount):
        if amount < 0: 
            print("Unable to withdraw")
        else:
            self.balance -= amount

account = BankAccount("Arun", 5000)

account.deposit(2000)

account.show_balance()
account.withdraw(100)


#Class attributes and methods

#8. Instance attribute vs class attribute

class Employee:

    company = "OpenAI"

    def __init__(self, name):
        self.name = name


employee1 = Employee("Arun")
employee2 = Employee("Priya")


print(employee1.name)
print(employee2.name)

print(employee1.company)
print(employee2.company)

#9. Class methods

class Employee:
    company = "TechCorp"
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

employee1 = Employee("Arun")
Employee.change_company("AI Solutions")

print(employee1.company)

#10. Static methods

class Calculator:
    @staticmethod
    def add(a,b):
        return a+b

Calculator.add(1,2)



#Encapsulation. Public, protected-style and private-style names

class Employee:

    def __init__(self):

        self.name = "Arun"       # Public
        self._salary = 50000     # Internal-use convention
        self.__password = "123"  # Name-mangled

#Properties — Controlled access

class BankAccount:

    def __init__(self, balance):

        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):

        if amount < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = amount


account = BankAccount(5000)

print(account.balance)

account.balance = 7000

print(account.balance)


#Inheritance

class Customer:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Welcome {self.name}")


class PremiumCustomer(Customer):

    def access_premium_features(self):
        print("Premium features activated")


customer = PremiumCustomer("Arun")

customer.greet()

customer.access_premium_features()

#super 
class Customer:

    def __init__(self, name, email):

        self.name = name
        self.email = email


class PremiumCustomer(Customer):

    def __init__(self, name, email, discount):

        super().__init__(name, email)

        self.discount = discount


customer = PremiumCustomer(
    "Arun",
    "arun@gmail.com",
    20
)

print(customer.name)
print(customer.email)
print(customer.discount)

#Polymorphism

class EmailNotification:

    def send(self):
        print("Sending email")


class SMSNotification:

    def send(self):
        print("Sending SMS")


class PushNotification:

    def send(self):
        print("Sending push notification")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]


for notification in notifications:
    notification.send()


#Abstraction

from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UpiPayment(PaymentProcessor):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CardPayment(PaymentProcessor):

    def pay(self, amount):
        print(f"Paid ₹{amount} using card")


upi = UpiPayment()
card = CardPayment()

upi.pay(1000)
card.pay(2000)

#Composition vs inheritance

class Address:

    def __init__(self, city, country):
        self.city = city
        self.country = country


class Customer:

    def __init__(self, name, address):

        self.name = name
        self.address = address


address = Address("Chennai", "India")

customer = Customer("Arun", address)

print(customer.name)
print(customer.address.city)