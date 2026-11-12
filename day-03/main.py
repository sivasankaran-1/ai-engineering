#list

customers = ["Arun", 28, 2500.50, True]
print(customers)

print(customers[0])
print(customers[1])
print(customers[-1])

print(customers[0:2])

#append

customers.append("Siva")
print(customers)

#extend

customers.extend(["Kumar", "John"])

#insert
customers.insert(1, "Priya")
print(customers)
#remove
customers.remove('Priya')
print(customers)

#pop
removed_customer = customers.pop()
print(customers)

#sort
numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)



print(numbers.count(10))

print(len(customers))

numbers[0] = 78
print(numbers)

#copy

a = [10, 20, 30]
b = a.copy()
b.append(40)

print(a)
print(b)

#------------------------------------------#

#TUPLES

customer_location = ("Chennai", "Tamil Nadu", "India")

print(customer_location)

print(customer_location[0])
print(customer_location[-1])


location = ("Chennai", "Tamil Nadu", "India")

location[0] = "Pondicherry"

print(location)


numbers = (10,)

print(type(numbers))

#Tuple unpacking

customer = ("Arun", 28, "Chennai")

name, age, city = customer

print(name)
print(age)
print(city)

#=======================================_
#SETS

customer_ids = {101, 102, 103, 101, 102, 104}
print(customer_ids)

#Adding
customer_ids.add(1)

#Adding multiple items
customer_ids.update([30, 40, 5])

#remove
numbers = {10, 20, 30}
numbers.remove(30)

numbers.discard(100)

print(numbers.discard(100))

#Union
purchase_customers = {101, 102, 103}
app_customers = {103, 104, 105}

all_customers = purchase_customers.union(app_customers)

print(all_customers)

#Intersection
premium_customers = {101, 102, 103}
repeat_customers = {102, 103, 104, 105}

loyal_customers = premium_customers.intersection(repeat_customers)

print(loyal_customers)

#Difference
new_customers = {104, 105, 106}
repeat_customers = {102, 103, 104, 105}

new_customers_only = new_customers.difference(repeat_customers)

print(new_customers_only)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.symmetric_difference(b))

#PART 4 — DICTIONARIES

customer = {
    "name": 'siva',
    "age": 27, 
    "email": 'siva@gmail.com'
}

customer["email"] = "arun@gmail.com"
print(customer) 

#del 

del customer["city"]

print(customer.get(name))

print(customer.keys())

print(customer.values())

print(customer.items())

for key, value in customer.items():
    print(key, value)
