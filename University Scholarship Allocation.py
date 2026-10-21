students = [
    {"name": "Lahari", "marks": 90, "subject": 80, "attendance": 95, "income": 150000},
    {"name": "Priya", "marks": 85, "subject": 75, "attendance": 90, "income": 200000},
    {"name": "Rahul", "marks": 90, "subject": 85, "attendance": 95, "income": 100000},
    {"name": "Arjun", "marks": 70, "subject": 60, "attendance": 80, "income": 300000}
]
eligible = []
for s in students:
    if s["marks"] >= 75 and s["subject"] >= 60 and s["attendance"] >= 75 and s["income"] <= 250000:
        eligible.append(s)
eligible.sort(key=lambda s: (-s["marks"], -s["subject"], -s["attendance"], s["income"]))
print("UNIVERSITY SCHOLARSHIP ALLOCATION")
print("---------------------------------")
for i, s in enumerate(eligible, start=1):
    print(i, s["name"], "- Marks:", s["marks"], 
          "Subject:", s["subject"], 
          "Attendance:", s["attendance"], 
          "Income:", s["income"])
print("\nTotal Eligible Students:", len(eligible))