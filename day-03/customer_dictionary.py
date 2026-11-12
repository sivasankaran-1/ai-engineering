
customer= {
    "name": "Siva",
    "age": 20,
}

print(customer["name"])

customer['age'] = 28

customer['email'] = "Siva@gmail.com"

print(customer)

phone = customer.get("phone", "Not provided")
print(phone)