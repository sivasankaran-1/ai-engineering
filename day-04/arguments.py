
def calculate_price(*prices):
    total = 0
    for price in prices:
        total += price
    return total

print(calculate_price(1,2,3,4,5))


def create_profile(**details):

    for key, value in details.items():
        print(f"{key}: {value}")



create_profile(
    name="Arun",
    experience=6,
    technology="React Native",
    learning="AI Engineering"
)