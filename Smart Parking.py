from datetime import datetime
print("===== SMART PARKING FEE MANAGEMENT =====")
vehicle = input("Enter vehicle type (Car/Bike): ").lower()
entry = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")
try:
    start = datetime.strptime(entry, "%H:%M")
    end = datetime.strptime(exit_time, "%H:%M")
    if vehicle not in ["car", "bike"]:
        print("Invalid vehicle type!")
    else:
        if end < start:
            end = end.replace(day=2)
        minutes = int((end - start).total_seconds() / 60)
        if minutes <= 0:
            print("Invalid parking duration!")
        else:
            hours = (minutes + 59) // 60
            if vehicle == "car":
                rate = 30
            else:
                rate = 15
            days = (hours + 23) // 24
            fee = min(hours * rate, days * 300)
            penalty = 100 if hours > 24 else 0
            total = fee + penalty
            print("\n===== PARKING BILL =====")
            print("Vehicle:", vehicle.title())
            print("Parking Hours:", hours)
            print("Overnight Parking:", "Yes" if end.date() != start.date() else "No")
            print("Parking Fee: Rs.", fee)
            print("Penalty: Rs.", penalty)
            print("Total Amount: Rs.", total)
except ValueError:
    print("Invalid time! Enter time in HH:MM format.")
