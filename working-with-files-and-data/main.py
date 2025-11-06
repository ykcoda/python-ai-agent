with open("./mac-address.txt", "rt") as f:
    content = f.read().split()
    unique_mac = set(list(content))


with open("./u_mac-address.txt", "a+") as f:
    for u in unique_mac:
        f.write(f"{u}\n")
