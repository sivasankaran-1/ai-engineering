#function 

def calculate_total(price1, price2):
    print("Total") 
    print (price1 + price2)

calculate_total(12, 12)


#Return vs print

def calculate_res(price1, price2):
    print("Total") 
    return (price1 + price2)

result = calculate_res(12, 12)
print("Res", result)    

#Types of function arguments

def introduce(name, age):
    print(f"this {name} and {age}")

introduce("siva", 28)

#Keyword arguments

def introduce(name, age):
    print(f"this {name} and {age}")

introduce(name = "siva", age = 28)

#7. Default arguments

def introduce(name = "Hey", age = 2):
    print(f"this {name} and {age}")

introduce(name = "", age = 28)

#*args and **kwargs

def calculate_sum(*args):

    total = 0

    for number in args:
        total += number

    return total


print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30))
print(calculate_sum(10, 20, 30, 40, 50))


#kwargs
def create_customer(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")


create_customer(
    name="Arun",
    age=28,
    city="Chennai",
    email="arun@gmail.com"
)


#Variable scope.  10. Local and global variables

name = "Arun"


def show_customer():
    customer_name = "Priya"

    print(customer_name)
    print(name)


show_customer()

print(name)

#Lambda functions

def square(number):
    return number * number


print(square(5))

#lambdaaaaa
square = lambda number: number * number

add = lambda a, b : a+b

print(add(1, 2))

#Example 2 — Check even or odd
even = lambda num : num % 2 == 0

#Sort customers by spending

customers = [
    {"name": "Arun", "spending": 2500},
     {"name": "Meena", "spending": 6000},
    {"name": "Priya", "spending": 4500},
   
]

sorted_customers = sorted(
    customers,
    key=lambda customer: customer["spending"], reverse=True
)

print(sorted_customers)

#Map, filter and reduce
#map() — Transform every element

prices = [100, 200, 300, 400]

taxed_prices = map(
    lambda price: price * 1.10,
    prices
)

print(list(taxed_prices))

#filter

spending = [500, 1500, 3000, 700, 5000]
high_spend = filter(lambda x: x > 1000, spending)

print(list(high_spend))


#reduce
from functools import reduce

total = reduce(lambda a, b : a + b, spending)

print(total)

#Comprehensions

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)

#List comprehensions — with conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)

#Transform and filter together
numbers = [1, 2, 3, 4, 5, 6]

result = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

print(result)

#Dictionary comprehension

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)

#Set comprehension

numbers = [1, 2, 2, 3, 3, 4]


squares = {
    number ** 2
    for number in numbers
}
print(squares)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    number
    for row in matrix
    for number in row
]

print(flattened)