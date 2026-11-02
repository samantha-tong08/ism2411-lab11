# Author: Samantha Tong
# Module 11 Lab: Customer Dictionary and Lookup

print("--- Exercise 1 ---")

customer = {
    "name": "Alice", # Key : Value ,
    "Name": "Not-Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("--- Exercise 2 ---")

customer["phone"] = '555-5555'
print(customer)
customer["tier"] = 'platinum'
print(customer)
del customer["Name"]
print(customer)

print(customer.get("ytd_spend",0))

print("--- Exercise 3 ---")

print(customer.get("email", "no email on file"))

print("--- Exercise 4 ---")

for key, value in customer.items(): 
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

print("--- Exercise 5 ---")

