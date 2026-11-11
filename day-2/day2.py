#conditions

age = 20

if age >= 20:
    print('You are an adult')
else:
    print('You are not an adult')


#Comparison operators

a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)


#The if, elif and else statements

age = 20

if age < 20:
    print("Hi")
elif age > 20:
    print("Hello")
else:
    print("Hey")

#Logical operators — AND, OR, NOT

age = 20
is_active = True

if age == 20  and is_active: 
    print("ok")



#PART 2 — LOOPS

for day in range (1, 8):
    print(f"Day {day} is a weekday")


#Multiplication table

number = 5

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


#while loop

while number > 0:
    print(number)
    number = number - 1


#break and continue

for number in range(1, 11):
    if number == 3:
        continue
    print(number)      


for number in range(1, 11):
    if number == 3:
        break
    print(number)    


#strings

name = "siva"
city = "Puducherry"
email = 'sivasankaran1598@gmail.com'

print(name[0:3])
print(name[::-1])

name = "PYTHON"
name = "python"
print(name.upper())

name = "arun kumar"

print(name.title())

email = "  arun@gmail.com  "
print(email.strip())

#replace
message = "I love JavaScript"
print(message.replace("JavaScript", "Python"))

#count
message = "banana"

print(message.count("a"))


#find
message = "I love Python"

print(message.find("Python"))


#startswith() and endswith()

email = "arun@gmail.com"

print(email.startswith("arun"))
print(email.endswith(".com"))


#isdigit()

age = "25"
print(age.isdigit())

