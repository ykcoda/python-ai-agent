def tail(filename, n=0):
    with open(filename, "rt") as file:
        content = file.readlines()

        for c in content[-n:]:
            print(c)


content = tail("./sample.txt", 1)
