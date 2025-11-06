with open("./devices.txt", "rt") as file:
    content = file.read().splitlines()
    device_list = list()
    for c in content[1:]:
        device_list.append(c.split(":"))

    print(device_list)
    print("#" * 80)
    for device in device_list:
        print(f"pinging.... {device[1]}")
