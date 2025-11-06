# Writing to a text file
with open("./config.txt", "wt") as file:
    file.write("Just a line.\n")
    file.write("Just a second line")


with open("./config.txt", "wt") as file:
    file.write("Just a line.\nJust a second line")

with open("./config1.txt", "at") as file:
    file.write("This is a new line.\n")
    file.write("This is a new line.\n")


with open("./config.txt", "r+") as file:
    file.write("Line as the beginning\n")

with open("./config.txt", "r+") as file:
    file.seek(10)
    file.write("Line as the beginning\n")
    file.seek(15)
    print(file.read())
