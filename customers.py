# Author: Samantha Tong
# Module 11 Lab: Customer Dictionary and Lookup

print("--- Reflection ---")

# 1. It's better to use .get() when a key doesn't exist in the dictionary and the value isn't as important, so it can just be set to a default value. An example would be if you were looking up a customer's phone number. It's better to use the bracket notation when a key is required. For example, looking up a customer's full name.
# 2. The pattern reminds me of a PivotTable in Excel. The Python version might be more useful for larger datasets because it can be ran automatically.

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

customers = [
   {"name": "Bob", "tier": "gold", "ytd_spend": 8750},
   {"name": "Charlie", "tier": "silver", "ytd_spend": 5000},
   {"name": "Diana", "tier": "platinum", "ytd_spend": 15000},
]

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

print("--- Exercise 8 ---")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print(sales_by_region)

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")