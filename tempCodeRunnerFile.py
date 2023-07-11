

details = {}

while True:
    name = input("Enter the name (or 'done' to exit): ")

    if name == 'done':
        break

    age = int(input("Enter the age: "))
    address = input("Enter the address: ")
    country = input("Enter the country: ")

    details[name] = {
        'age': age,
        'address': address,
        'country': country
    }

print(details)

    