with open("./sample.txt", "rt") as f:
    total = 0
    content = f.read().split()
    for c in content:
        data = c.split(":")
        if data[0].lower() == "d":
            total += int(data[1])
        else:
            total -= int(data[1])
    print(f"Total: {total}")
