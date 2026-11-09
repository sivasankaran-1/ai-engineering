print("Hello Ai Enginner")

age = 25
name = "Siva"
salary = "25000"

print(age)
print(name)
print(salary)


#Data Types 

#Integer

age = 23
total_customers = 100
quantity = 3

print(age)
print(type(age))

#Float
weight = 55.6
price = 99.99

print(weight)
print(type(weight))

#String 
name = "Siva"
city  = 'puducherry'

print(name)
print(city)

print(type(name))

#Boolean

is_active = True
print(type(is_active))

#Check the data type using type()

customer_name = "Siva"
customer_age = 28
customer_balance = 3500
is_subscribed = True

print(type(customer_name))
print(type(customer_age))
print(type(customer_balance))
print(type(is_subscribed))


#dynamic typing

x = 10
print(x)
print(type(x))

x = "Siva"
print(x)
print(type(x))


#type int
age: int = 27
name: str = "siva"
salary: float = 36.00
is_active = True

print(age)
print(name)
print(salary)
print(is_active)

#function example 

def calculate_salary(salary: float)-> float:
    return salary * 2

annual_salary = calculate_salary(50000)
  
print(annual_salary)


#Type conversion

{
  "age": "25",
  "salary": "50000.50"
}

#String to integer

age = "25"
age = int(age)
print(age)
print(type(age))

#String to float
age = "25"
age = float(age)
print(age)
print(type(age))

#integer to string
age = 25
age = str(age)
print(age)
print(type(age))

#F-strings

name = "Siva"
age = 25

message = f"this is my {name} and {age}"
print(message)