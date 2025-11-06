# f = open("./config.txt")

# .  => current working directory
# .. => parent directory
# f = open("./config.txt", "rt")
# content = f.read(5)
# print(content)

# content = f.read(3)
# print(content)

# print(f.tell())

# f.seek(2)
# print(f.read(2))

# f.seek(0)
# print(f.read(5))
f = open("./config.txt")
print(f.read())

# do stuff
print("#" * 20)
f.seek(0)
print(f.read())
