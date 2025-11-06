with open("./config.txt", "rt") as file:
    content = file.read()
    print(content)

    print(file.closed)
    file.seek(0)
    print(file.read())

print(f"closed? {file.closed}")
