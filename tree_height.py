def process_tree(start_index, nodes):
    zzz = 0
    aaa = []

    l = 0
    for i in nodes:
        if i == start_index:
            aaa.append(l)
        l = l + 1

    if len(aaa) == 0:
        return 1

    for k in aaa:
        zzz = max(process_tree(k, nodes), zzz)

    return zzz + 1


def main():
    choice  = input()

    if "F" in choice:
        filename = input()
        useFile = filename + '.txt'
        file1 = open(useFile, 'r')
        Lines = file1.readlines()

        amount = Lines[0]
        tree = Lines[1]

    elif "I" in choice:

        amount = input()
        tree = input()

    tree = tree.split(" ")
    tree = [int(i) for i in tree]
    start_index = 0

    c = 0
    for a in tree:
        if a == -1:
            start_index = c

        c = c + 1

    # nodes = numpy.array([4, -1, 4, 1, 1])
    # start_index = 1

    zzz = process_tree(start_index, tree)

    print(tree)

    print(zzz)


if __name__ == '__main__':
    main()
    