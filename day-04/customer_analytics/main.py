
from analytics import (
    get_active_customers,
    get_total_spending,
    get_average_spending,
    get_high_spending_customers,
    get_customer_names,
    get_unique_cities,
    get_highest_spender,
    find_customer_by_id,
    calculate_total_for_active_customers
)


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


print("========== CUSTOMER ANALYTICS ==========")

print("\nAll customer names:")
print(get_customer_names(customers))


print("\nActive customers:")
print(get_active_customers(customers))


print("\nTotal spending:")
print(get_total_spending(customers))


print("\nAverage spending:")
print(get_average_spending(customers))


print("\nHigh spending customers:")
print(get_high_spending_customers(customers))


print("\nUnique cities:")
print(get_unique_cities(customers))


print("\nHighest spender:")
print(get_highest_spender(customers))


print("\nCustomer search: ID 103")
print(find_customer_by_id(customers, 103))


print("\nActive customer spending:")
print(calculate_total_for_active_customers(customers))
