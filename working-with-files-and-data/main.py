with open("./sample1.txt") as f:
    content1 = set(f.read().split())
    print(content1)


with open("./sample2.txt") as f1:
    content2 = set(f1.read().split())
    print(content2)

unique1 = content1.difference(content2)
print(unique1)
unique2 = content2.difference(content1)
print(unique2)
