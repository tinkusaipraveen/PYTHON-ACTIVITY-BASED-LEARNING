scores = [90, 80, 70, 60, 50, 40]
group_size = 2

scores.sort(reverse=True)
groups = [[] for _ in range(len(scores) // group_size)]
totals = [0] * len(groups)

for score in scores:
    i = totals.index(min(totals))
    if len(groups[i]) < group_size:
        groups[i].append(score)
        totals[i] += score
    else:
        for j in range(len(groups)):
            if len(groups[j]) < group_size:
                groups[j].append(score)
                totals[j] += score
                break

for i in range(len(groups)):
    print("Group", i + 1, ":", groups[i], "Total:", totals[i])