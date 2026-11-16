print("Application started")

result = 10 
print("Application finished")

#value Error

number = int("hello")
print(number)

#Part 2 — try, except, else and finally

try:
    number = int(input("Enter the number"))
    print(number)
except ValueError:
    print("This is valiue error")

#Multiple except blocks

try:

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

    print(result)

except ValueError:

    print("Only numbers are allowed")

except ZeroDivisionError:

    print("Cannot divide by zero")

#The else block

try:
    number = int(input("Enter the number"))
    print('ik')
    
except ValueError:
    print("this is a value error")
else:
    print('This is else block')

#The finally block

try:

    file = open("example.txt", "r")

    print(file.read())

except FileNotFoundError:

    print("File does not exist")

finally:

    print("Operation completed")


#===================================

try:

    number = int(input("Enter a number: "))

    result = 100 / number

except ValueError:

    print("Enter a valid integer")

except ZeroDivisionError:

    print("Number cannot be zero")

else:

    print("Result:", result)

finally:

    print("Program execution completed")



#Raising exceptions

def deposit(amount):
    if amount <= 0:
        raise ValueError("Amount canniot be negative")
    print('Deposited')

deposit(-11)

#10. Create custom exceptions

class InsufficientBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient account balance")

        amount -= self.balance

account = BankAccount(-11)

try:
 account.withdraw(100) 
except InsufficientBalanceError as error:
    print("Transaction failed:", error)


#EException chaining

import json

try:

    json.loads("{invalid}")

except json.JSONDecodeError as error:

    raise RuntimeError(
        "Unable to load customer data"
    ) from error


#Working with files

file = open("customers.txt", "w")

file.write("Arun\n")
file.write("Priya\n")

file.close()


#append
file = open("customers.txt", "a")

file.write("Meena\n")

file.close()

#Read

file = open("customers.txt", "r")

content = file.readlines()
file.readline()   # Reads one line
file.readlines()  # Returns all lines as a list
file.read() 

print(content)

file.close()

#Why use with

with open("customers.txt", "r", encoding="utf-8") as file:

    content = file.read()

    print(content)

#pathlib

from pathlib import Path

file_path = Path("data") / "customers.txt"

print(file_path)

#Create directories:
file_path.parent.mkdir(parents=True, exist_ok=True)

if file_path.exists():
    print("File exists")
else:
    print("File does not exist")

#write text
    file_path.write_text(
    "Arun\nPriya\n",
    encoding="utf-8"
)

#read text 
content = file_path.read_text(encoding="utf-8")

print(content)

#read lines
lines = file_path.read_lines(encoding="utf-8")

print(lines)

#JSON: essential for AI engineering

{
  "name": "Arun",
  "age": 28,
  "is_active": True
}

#Python's json module
import json

customer = {
     "name": "Arun",
    "age": 28,
    "is_active": True
}

json_data = json.dumps(customer,  indent=4)
print(json_data)

print(type(json_data))

#Deserialization.  Deserialization converts JSON text back into a Python object.

import json

json_data = """
{
    "name": "Arun",
    "age": 28,
    "city": "Chennai"
}
"""

customer = json.loads(json_data)

print(customer)

print(type(customer))

#Write JSON to a file

import json

customers = [
    {
        "id": 101,
        "name": "Arun",
        "city": "Chennai"
    },
    {
        "id": 102,
        "name": "Priya",
        "city": "Pondicherry"
    }
]

with open("customers.json", "w", encoding="utf-8") as file:

    json.dump(
        customers,
        file,
        indent=4,
        ensure_ascii=False
    )

#
import json

with open("customers.json", "r", encoding="utf-8") as file:

    customers = json.load(file)


for customer in customers:

    print(customer["name"])

#Handle invalid JSON

import json

try:

    with open("customers.json", "r", encoding="utf-8") as file:

        customers = json.load(file)

except FileNotFoundError:

    print("Customer file not found")

except json.JSONDecodeError as error:

    print("Invalid JSON:", error)

else:

    print("Customers loaded:", len(customers))



