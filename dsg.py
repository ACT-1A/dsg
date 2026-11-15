print("============GROCERY RECEIPT============")
name = input("Enter Customer Name: ")
item = input("Enter Item Name: ")
price = float(input("Enter Price: "))
qty = int(input("Enter Quantity: "))
print("\n==============RECEIPT=================")
print(f"Customer Name: {name}")
print(f"Price : P{price:.2f}")
print(f"Quantity : {qty}")
total_cost = price * qty
print(f"Total Cost : P{total_cost:.2f}")
vat = total_cost * 0.12
print(f"VAT (12%): P{vat:.2f}")
amount = total_cost + vat
print(f"Amount to Pay: P{amount:.2f}")
print("\n=======================================")