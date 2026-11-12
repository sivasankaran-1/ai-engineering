from functools import reduce
numbers = [10, 20, 30, 40, 50]

squared_numbers = map(lambda x: x**2, numbers)

filtered_numbers = filter(lambda x: x > 10, numbers)

reduced_value = reduce(lambda x, y: x + y, numbers)

print(list(squared_numbers))   
print(list(filtered_numbers))
print(reduced_value)