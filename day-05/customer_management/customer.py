
class Customer:

    customer_count = 0

    def __init__(
        self,
        customer_id,
        name,
        email,
        city,
        monthly_spending=0.0,
        is_active=True
    ):

        if not name.strip():
            raise ValueError("Customer name is required")

        if not self.is_valid_email(email):
            raise ValueError("Invalid email address")

        if monthly_spending < 0:
            raise ValueError("Spending cannot be negative")

        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.city = city
        self._monthly_spending = monthly_spending
        self.is_active = is_active

        Customer.customer_count += 1

    @staticmethod
    def is_valid_email(email):

        if not isinstance(email, str):
            return False

        if "@" not in email:
            return False

        local, domain = email.split("@", 1)

        return bool(local and "." in domain and not domain.startswith("."))

    @property
    def monthly_spending(self):
        return self._monthly_spending

    @monthly_spending.setter
    def monthly_spending(self, amount):

        if amount < 0:
            raise ValueError("Spending cannot be negative")

        self._monthly_spending = amount

    def update_spending(self, amount):

        if amount < 0:
            raise ValueError("Amount cannot be negative")

        self.monthly_spending += amount

    def deactivate(self):
        self.is_active = False

    def activate(self):
        self.is_active = True

    def to_dict(self):

        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "city": self.city,
            "monthly_spending": self.monthly_spending,
            "is_active": self.is_active
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            customer_id=data["customer_id"],
            name=data["name"],
            email=data["email"],
            city=data["city"],
            monthly_spending=data.get("monthly_spending", 0.0),
            is_active=data.get("is_active", True)
        )


class CustomerManager:

    def __init__(self):
        self._customers = []

    @property
    def customers(self):
        # Return an immutable snapshot of the collection.
        return tuple(self._customers)

    def add_customer(self, customer):

        if not isinstance(customer, Customer):
            raise TypeError("Expected a Customer object")

        if self.get_customer_by_id(customer.customer_id):
            raise ValueError("Customer ID already exists")

        self._customers.append(customer)

    def get_customer_by_id(self, customer_id):

        for customer in self._customers:

            if customer.customer_id == customer_id:
                return customer

        return None

    def get_active_customers(self):

        return [
            customer
            for customer in self._customers
            if customer.is_active
        ]

    def get_customers_by_city(self, city):

        return [
            customer
            for customer in self._customers
            if customer.city.lower() == city.lower()
        ]

    def get_total_spending(self):

        return sum(
            customer.monthly_spending
            for customer in self._customers
        )

    def get_average_spending(self):

        if not self._customers:
            return 0

        return self.get_total_spending() / len(self._customers)

    def get_highest_spender(self):

        if not self._customers:
            return None

        return max(
            self._customers,
            key=lambda customer: customer.monthly_spending
        )

    def deactivate_customer(self, customer_id):

        customer = self.get_customer_by_id(customer_id)

        if customer is None:
            return False

        customer.deactivate()

        return True
