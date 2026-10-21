production = [
    [1000, 20],
    [800, 50],
    [1200, 30],
    [500, 40]
]

limit = 5

for i in range(len(production)):
    total = production[i][0]
    defective = production[i][1]

    percentage = (defective / total) * 100

    print("Batch", i + 1)
    print("Defect Percentage:", percentage, "%")

    if percentage > limit:
        print("Quality Alert!")
    else:
        print("Quality Accepted")