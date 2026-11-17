#Decorator
#Without a decorator

def greet():
    print("Hello!")

greet()

#1.2 Your first decorator

def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def greet1():
    print("Hello!111")



greet1()

#1.3 The @ syntax The @my_decorator syntax is equivalent to:
greet = decorator(greet)

@decorator
def greet2():
    print('greet 2')

greet2()

#Decorators with arguments
def my_decorator(func):

    def wrapper(*args, **kwargs):

        print("Before execution")

        result = func(*args, **kwargs)

        print("After execution")

        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)

#1.5 Preserve function metadata with functools.wraps

from functools import wraps


def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")

        result = func(*args, **kwargs)

        return result

    return wrapper


@log_execution
def calculate_total(price, quantity):
    """Calculate total price."""
    return price * quantity


print(calculate_total(100, 3))
print(calculate_total.__name__)
print(calculate_total.__doc__)

#Practical decorator: retry

from functools import wraps


def retry(max_attempts=3):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for attempt in range(1, max_attempts + 1):

                try:
                    return func(*args, **kwargs)

                except (TimeoutError, ConnectionError):

                    if attempt == max_attempts:
                        raise

                    print(
                        f"Retrying... {attempt}/{max_attempts}"
                    )

        return wrapper

    return decorator


@retry(max_attempts=3)
def call_ai_api():
    print("Calling AI API...")
    return "AI response"


print(call_ai_api())

#2. Iterators: moving through data one item at a time

number = [1, 3, 4]

iterator = iter(number)

print(next(iterator))

#2.2 How a for loop works internally
for number in [1, 2, 3]:
    print(number)

#Build your own iterator

class NumberIterator:

    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):

        if self.current > self.limit:
            raise StopIteration

        value = self.current
        self.current += 1

        return value


numbers = NumberIterator(5)

for number in numbers:
    print(number)

#3. Generators: processing data lazily

#3.1 Normal function versus generator
def get_numbers():
    return [1, 2, 3]


numbers = get_numbers()

print(numbers)

#yield
def get_numbers():
    yield 1
    yield 2
    yield 3


numbers = get_numbers()

print(next(numbers))
print(next(numbers))
print(next(numbers))