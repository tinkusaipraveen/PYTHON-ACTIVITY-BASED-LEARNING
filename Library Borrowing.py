books = [
    ("B101", 7, 2),
    ("B102", 5, 0),
    ("B103", 10, 4)
]

fine_rate = 5
available_books = 0

for book_id, borrowed_days, late_days in books:
    fine = late_days * fine_rate

    if late_days > 0:
        print(book_id, "- Overdue! Fine: Rs.", fine)
    else:
        print(book_id, "- Returned on time")

    if late_days == 0:
        available_books += 1

print("Books available:", available_books)