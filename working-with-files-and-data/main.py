with open("./sample.txt", "r") as file:
    content = file.read().split()


with open("./_sample.txt", "w") as f:
    for c in content:
        f.write(f"{c}\n")
