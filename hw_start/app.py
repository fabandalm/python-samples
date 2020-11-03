def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


def increment(number, by=1):
    return number + by


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


def save_user(**user):
    print(user)
    print(user["id"])


greet("John", 'Smith')

result = increment(7)
print(result)
print(multiply(1,2,3,4,5))

save_user(id=1,name="John")

