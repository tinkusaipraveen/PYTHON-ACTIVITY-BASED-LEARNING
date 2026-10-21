routes = [
    ("Route A", 100, 40),
    ("Route B", 75, 30),
    ("Route C", 25, 20)
]

for route, passengers, capacity in routes:
    buses = (passengers + capacity - 1) // capacity
    served = buses * capacity
    unserved = max(0, passengers - served)

    print("Route:", route)
    print("Buses Required:", buses)
    print("Unserved Passengers:", unserved)
    print()