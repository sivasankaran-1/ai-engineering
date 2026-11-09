monthly_salary: float = 50000

def calculate_annual_salary(salary: float)-> float:
    return salary * 12

def calculate_bonus_salary(salary: float)-> float:
    return calculate_annual_salary(salary) * 0.10

def total_compensation(monthly_salary: float)-> float:
    return calculate_annual_salary(monthly_salary) + calculate_bonus_salary(monthly_salary)

print(f"Annual salary: {calculate_annual_salary(monthly_salary)}")
print(f"Bonus: {calculate_bonus_salary(monthly_salary)}")
print(f"Total compensation: {total_compensation(monthly_salary)}")

# Annual salary: 600000
# Bonus: 60000
# Total compensation: 660000