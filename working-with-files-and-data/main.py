with open("./sample.txt", "r") as f:
    content = f.read().splitlines()

    my_string = "\n".join(content)
    print(my_string)
