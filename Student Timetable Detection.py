print("===== STUDENT TIMETABLE CONFLICT DETECTION =====")
# Course schedules as tuples
schedule = [
    ("Python", "09:00", "10:00", "Room1"),
    ("Java", "09:30", "10:30", "Room2"),
    ("Maths", "11:00", "12:00", "Room3")
]

unavailable_rooms = ["Room3"]

# Check timetable conflicts
for i in range(len(schedule)):
    course1, start1, end1, room1 = schedule[i]

    for j in range(i + 1, len(schedule)):
        course2, start2, end2, room2 = schedule[j]

        if start1 < end2 and start2 < end1:
            print("Time Conflict:", course1, "and", course2)

# Check unavailable rooms
for course, start, end, room in schedule:
    if room in unavailable_rooms:
        print("Unavailable Room:", course, "uses", room)

# Validate timetable
conflict = False

for i in range(len(schedule)):
    for j in range(i + 1, len(schedule)):
        if schedule[i][1] < schedule[j][2] and schedule[j][1] < schedule[i][2]:
            conflict = True

for course, start, end, room in schedule:
    if room in unavailable_rooms:
        conflict = True

if conflict:
    print("Timetable is INVALID")
else:
    print("Timetable is VALID")