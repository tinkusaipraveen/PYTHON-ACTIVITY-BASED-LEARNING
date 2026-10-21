seating = [
    [101, 102, 103],
    [104, 0, 105],
    [106, 102, 108]
]

reserved = [(1, 1)]
roll_numbers = []

for i in range(len(seating)):
    for j in range(len(seating[i])):
        roll = seating[i][j]

        if (i, j) in reserved and roll != 0:
            print("Reserved seat occupied:", i, j)

        if roll == 0:
            print("Empty seat:", i, j)
        elif roll in roll_numbers:
            print("Duplicate roll number:", roll)
        else:
            roll_numbers.append(roll)

print("Seating Validation Completed")