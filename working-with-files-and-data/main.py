def get_file_details(f):
    with open(f) as file:
        c1 = file.read().splitlines()
        print(c1)
        print(f"Total lines: {len(c1)}")
        print("#" * 50)

        words = 0
        for l in list(c1):
            words += len(l.split())

        print(f"Total Words: {words}")

        print("#" * 50)
        s1 = "".join(c1)
        print(f"Total Charaters: {len(list(s1))}")


ff = get_file_details("./sample.txt")


def wc(file):
    with open(file, "r") as f:
        # reading the file into a list
        content = f.read().splitlines()

        lines = len(content)

        words = 0
        for line in content:
            words += len(line.split())

        chars = 0
        for line in content:
            chars += len(list(line))

        return lines, words, chars


print(wc("./sample.txt"))
