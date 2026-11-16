import json
product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000,
    "in_stock": True
}

json_dump = json.dumps(product)

print(json_dump)
print(type(json_dump))


load = json.loads(json_dump)
print(load)
print(type(load))

with open("product.json", 'w') as file:
    json.dump(product, file, indent=4)

with open("product.json", 'r') as file:
      customers = json.load(file)

print(customers)