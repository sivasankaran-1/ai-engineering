customers = [
    {"id": 1, "name": "Arun", "active": True},
    {"id": 2, "name": "Priya", "active": False},
    {"id": 3, "name": "Kumar", "active": True},
    {"id": 4, "name": "John", "active": False},
    {"id": 5, "name": "Meena", "active": True}
]

active_customer = []

for customer in customers:
    if customer['active'] == True:
        active_customer.append(customer)

print(active_customer)
print(len(active_customer))

print(len(customers) - len(active_customer))