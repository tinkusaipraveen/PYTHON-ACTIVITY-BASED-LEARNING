stock = {"burger": 10, "pizza": 5, "juice": 8}
price = {"burger": 50, "pizza": 100, "juice": 30}
sales = 0

while True:
    item = input("Enter item name (or stop): ").lower()

    if item == "stop":
        break

    if item not in stock:
        print("Item not available!")
        continue

    qty = int(input("Enter quantity: "))

    if qty <= 0:
        print("Invalid quantity!")
    elif qty > stock[item]:
        print("Insufficient stock!")
    else:
        bill = qty * price[item]
        stock[item] -= qty
        sales += bill
        print("Bill: Rs.", bill)

print("Total Sales: Rs.", sales)
print("Remaining Stock:", stock)