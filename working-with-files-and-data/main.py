with open("./sample1.txt") as file:
    content = file.read().split()
    print(content)

    my_dict = {}

    for c in content:
        my_dict[c] = len(c)

    print(my_dict)
