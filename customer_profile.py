customer_name: str = "Siva"
customer_id: int= 123
customer_city: str = "Py"
account_balance: float = 2000
customer_age: int = 28
monthly_spending: float = 2500.75
is_premium_member: bool = True
total_orders: int = 15

# Calculate yearly spending
yearly_spending: float = monthly_spending * 12


# Calculate average spending
average_spending: float = monthly_spending / 12

# Customer profile summary
print("========== CUSTOMER PROFILE ==========")

print(f"Name: {customer_name}")
print(f"Age: {customer_age}")
print(f"Monthly Spending: ₹{monthly_spending}")
print(f"Yearly Spending: ₹{yearly_spending}")
print(f"Premium Member: {is_premium_member}")
print(f"Total Orders: {total_orders}")
print(f"Average Spending: ₹{average_spending}")

print("======================================")