
from functools import reduce


def get_active_customers(customers):
    """Return only active customers."""

    return [
        customer
        for customer in customers
        if customer["is_active"]
    ]


def get_total_spending(customers):
    """Calculate total spending."""

    return reduce(
        lambda total, customer:
            total + customer["monthly_spending"],
        customers,
        0
    )


def get_average_spending(customers):
    """Calculate average customer spending."""

    if not customers:
        return 0

    total = get_total_spending(customers)

    return total / len(customers)


def get_high_spending_customers(customers, threshold=3000):
    """Find customers spending above a threshold."""

    return list(
        filter(
            lambda customer:
                customer["monthly_spending"] > threshold,
            customers
        )
    )


def get_customer_names(customers):
    """Extract customer names."""

    return [
        customer["name"]
        for customer in customers
    ]


def get_unique_cities(customers):
    """Find unique customer cities."""

    return {
        customer["city"]
        for customer in customers
    }


def get_highest_spender(customers):
    """Return the customer with highest spending."""

    if not customers:
        return None

    return max(
        customers,
        key=lambda customer: customer["monthly_spending"]
    )


def find_customer_by_id(customers, customer_id):
    """Find a customer by ID."""

    return next(
        (
            customer
            for customer in customers
            if customer["id"] == customer_id
        ),
        None
    )


def calculate_total_for_active_customers(customers):
    """Calculate spending for active customers only."""

    active_customers = get_active_customers(customers)

    return get_total_spending(active_customers)
