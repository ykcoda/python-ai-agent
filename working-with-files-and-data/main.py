import csv


with open("sample.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Grade"])

    models = [
        ("Kwame", 23, "A"),
        ("Kofi", 12, "B"),
        ("Kwame", 76, "C"),
        ("Kwame", 53, "A"),
    ]

    for model in models:
        writer.writerow(model)


data = [["Name", "Age"], ["ama", 12], ["kofi", 11]]
with open("tab_logs.csv", "w") as csv_file:
    writer = csv.writer(csv_file)

    writer.writerows(data)
