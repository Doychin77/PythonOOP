def read_next(*args):
    for word in args:
        for ch in word:
            yield ch

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)

