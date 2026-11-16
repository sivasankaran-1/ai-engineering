
def calculator(a, b, operation):
    try:
        if operation == "Add":
            return a + b 
        elif operation == "Sub":
            return a - b 
        elif operation == "Mul":
            return a * b 
        elif operation == "Div":
            try:
             return a / b 
            except ZeroDivisionError:
                print("zero divisible error")
    except ValueError:
        print("Thois is value Error")

calculator(2,0, "Div")