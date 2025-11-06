with open("./sample1.txt") as file:
    content = file.read().split()

    my_dict = {}

    for c in content:
        my_dict[c] = len(c)

    # s_my_dict = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

    nn = sorted(my_dict.items())
    ss = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

    print(ss[:100])
