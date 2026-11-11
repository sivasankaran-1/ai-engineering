password = "Python123"

has_minimum_length = len(password) >= 8
has_number = any(char.isdigit() for char in password)


if has_minimum_length and has_number:
     print("Basic password requirements satisfied")
else:
     print("Password does not meet requirements")
