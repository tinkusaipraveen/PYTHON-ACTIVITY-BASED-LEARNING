transactions = [
    (101, 500, "deposit"),
    (102, 200, "withdraw"),
    (101, 300, "deposit"),
    (103, -100, "withdraw"),
    (104, 1000, "withdraw")
]

ids = []

for t in transactions:
    if t[0] in ids:
        print("Duplicate ID:", t[0])
    else:
        ids.append(t[0])

    if t[1] <= 0:
        print("Invalid amount:", t)

    if t[2] not in ["deposit", "withdraw"]:
        print("Invalid transaction type:", t)

    if t[2] == "withdraw" and t[1] > 800:
        print("Suspicious transaction:", t)

print("Audit Completed")