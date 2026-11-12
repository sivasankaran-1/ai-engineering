# ==========================================
# CUSTOMER DATA MANAGEMENT SYSTEM
# ==========================================

customers = [
    {
        "id": 101,
        "name": "Arun",
        "age": 28,
        "city": "Chennai",
        "monthly_spending": 2500.0,
        "is_active": True
    },
    {
        "id": 102,
        "name": "Priya",
        "age": 25,
        "city": "Pondicherry",
        "monthly_spending": 4500.0,
        "is_active": True
    },
    {
        "id": 103,
        "name": "Kumar",
        "age": 32,
        "city": "Chennai",
        "monthly_spending": 800.0,
        "is_active": False
    },
    {
        "id": 104,
        "name": "Meena",
        "age": 29,
        "city": "Bangalore",
        "monthly_spending": 6000.0,
        "is_active": True
    },
    {
        "id": 105,
        "name": "John",
        "age": 35,
        "city": "Chennai",
        "monthly_spending": 1200.0,
        "is_active": False
    }
]

def display_customers():
    for customer in customers:
         print(
            f"ID: {customer['id']} | "
            f"Name: {customer['name']} | "
            f"City: {customer['city']} | "
            f"Spending: ₹{customer['monthly_spending']} | "
            f"Active: {customer['is_active']}"
        )

display_customers()

def find_customer():
    for customer in customers:
        if customer['id'] == 104:
            print(f"Customer is:{customer['name']}")
      

find_customer()

def active_customers():
    for customer in customers:
        if customer['is_active']:
            print(f"Customer is:{customer['name']}")
      

active_customers()

def total_spending():
    total_spending  = 0
    for customer in customers:
       total_spending = total_spending + customer["monthly_spending"]
    print(total_spending)

total_spending()


def find_unique_cities():

    cities = set()

    for customer in customers:
        cities.add(customer["city"])

    return cities

def find_high_spending_customers():

    print("\n========== HIGH-SPENDING CUSTOMERS ==========")

    for customer in customers:

        if customer["monthly_spending"] >= 3000:
            print(customer["name"])

find_high_spending_customers()