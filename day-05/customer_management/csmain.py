
from customer import Customer, CustomerManager


manager = CustomerManager()


# Create customer objects

customer1 = Customer(
    101,
    "Arun",
    "arun@gmail.com",
    "Chennai",
    2500
)

customer2 = Customer(
    102,
    "Priya",
    "priya@gmail.com",
    "Pondicherry",
    4500
)

customer3 = Customer(
    103,
    "Meena",
    "meena@gmail.com",
    "Bangalore",
    6000
)

customer4 = Customer(
    104,
    "Kumar",
    "kumar@gmail.com",
    "Chennai",
    800
)


# Add customers

manager.add_customer(customer1)
manager.add_customer(customer2)
manager.add_customer(customer3)
manager.add_customer(customer4)


# Update spending

customer1.update_spending(500)


# Deactivate a customer

manager.deactivate_customer(104)


# Display analytics

print("========== CUSTOMER MANAGEMENT ==========")

print("\nTotal customers:")
print(len(manager.customers))


print("\nActive customers:")

for customer in manager.get_active_customers():
    print(customer.name)


print("\nCustomers from Chennai:")

for customer in manager.get_customers_by_city("Chennai"):
    print(customer.name)


print("\nTotal spending:")
print(manager.get_total_spending())


print("\nAverage spending:")
print(round(manager.get_average_spending(), 2))


print("\nHighest spender:")
highest = manager.get_highest_spender()

if highest:
    print(highest.name, highest.monthly_spending)


print("\nCustomer count created:")
print(Customer.customer_count)


print("\nCustomer 101 as dictionary:")
print(customer1.to_dict())
