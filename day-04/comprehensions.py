numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Squares
squares = [
    number ** 2
    for number in numbers
]
print(squares)

# 2. Even numbers
even_numbers = [
    numbers
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)


# 3. Dictionary comprehension
number_dictionary = {
    number: number ** 2
    for number in numbers
}

print("Dictionary:", number_dictionary)


# 4. Set comprehension

even_numbers_set = {
    number
    for number in numbers
    if number % 2 == 0
}

print("Set:", even_numbers_set)

# 5. Filter and transform
result = [
    number * 10
    for number in numbers
    if number > 5
]

print("Filtered and transformed:", result)