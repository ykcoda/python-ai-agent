# Reading file into list

# example 1
my_list = []

with open("./config.txt", "rt") as file:
    content = file.read().splitlines()
    for c in content:
        my_list.append(c)


# example 2

with open("./config.txt", "rt") as file:
    content = file.readlines()
    content[0] = "PORT=7777"
    print(content[0])

# example 3
with open("./config.txt", "rt") as file:
    content = list(file)
    print(content)

# Iterate over a file
with open("./config.txt", "rt") as file:
    for f in file:
        print(f, end=" ")
