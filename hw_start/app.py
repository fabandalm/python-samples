def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


def increment(number, by=1):
    return number + by


greet("John", 'Smith')
result = increment(7)
print(result)