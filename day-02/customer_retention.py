# ==========================================
# CUSTOMER RETENTION RULE ENGINE
# ==========================================


# Customer information

customer_name = "  arun kumar  "
customer_age = 28
days_since_last_login = 20
monthly_spending = 300.0
support_tickets = 4
login_pattern = "1010010"

# Clean customer information

customer_name = customer_name.strip().title()

print(customer_name)

# Initialize risk score


print("========== CUSTOMER REPORT ==========")

print(f"Customer Name: {customer_name}")
print(f"Customer Age: {customer_age}")
print(f"Days Since Last Login: {days_since_last_login}")
print(f"Monthly Spending: ₹{monthly_spending}")
print(f"Support Tickets: {support_tickets}")

# Rule 1: Inactivity
risk_score = 0
if days_since_last_login>=14:
    risk_score += 2
    print("Warning: Customer inactive for 14+ days")

elif days_since_last_login >= 7:
    risk_score += 1
    print("Warning: Customer inactive for 7+ days")

# Rule 2: Low spending
if monthly_spending < 500:
    risk_score += 1
    print("Warning: Low customer spending")


# Rule 3: Support tickets
if support_tickets >= 3:
    risk_score += 1
    print("Warning: Multiple support tickets")

# Rule 4: Weekly login activity
active_days = 0
day_number = 1

for login in login_pattern:
    if login == "1":
        active_days = active_days+1
        print(f"Day {day_number}: Logged in")

    else:
        print(f"Day {day_number}: No login")

    day_number += 1

if active_days < 3:
    risk_score += 2


# Final risk classification

print("\n========== RISK ASSESSMENT ==========")

print(f"Total Risk Score: {risk_score}")

if risk_score >= 4:
    risk_level = "HIGH"

elif risk_score >= 2:
    risk_level = "MEDIUM"

else:
    risk_level = "LOW"

print(f"Customer Churn Risk: {risk_level}")

print("=====================================")