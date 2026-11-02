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

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")

print("--- Exercise 6 ---")

# customers = [
#   {"name": "Alice", "tier": "gold"},
# ]

for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase")

print("--- Exercise 7 ---")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {name} - only {details['stock']} left")