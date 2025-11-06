import time


def tail(filename, n=0):
    with open(filename, "rt") as file:
        content = file.readlines()

        for c in content[-n:]:
            print(c)


while True:
    time.sleep(3)
    content = tail("./sample.txt", 5)
    print("#" * 50)
