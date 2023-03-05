

# python3

import sys
import threading
import numpy


def compute_height(sq, parents):
    # Write this function
    max_height = 0
    # Your code here
    return max_height


def process_tree(start_index, nodes):
    zzz = 0
    aaa = []

    l = 0
    for i in nodes:
        if i == start_index:
            aaa.append(l)
        l = l + 1

    if aaa.count == 0:
        return 1

    for k in aaa:
        zzz = max(process_tree(k, nodes), zzz)

    return zzz + 1


def main():
    amount = input()
    tree = input().split(" ")
    tree = [int(i) for i in tree]

    c = 0
    for a in tree:
        if a == -1:
            start_index = c

        c = c + 1

    # nodes = numpy.array([4, -1, 4, 1, 1])
    # start_index = 1
    #
    zzz = process_tree(start_index, tree)
    #
    print(zzz)

    #
    # # implement input form keyboard and from files
    #
    # # choice = input()
    #
    # # amount, array = input().splitlines()
    # #
    # # print(amount)
    # # print(array)
    #
    # amount = 5
    # num = numpy.array([4, -1, 4, 1, 1])
    # #                  0   1  2  3  4
    #
    # #                        1
    # #                      3   4
    # #                         0  2
    #
    # levels = compute_height(amount, num)
    #
    # # array = []
    # # print('a')
    # #
    # # arr = input()
    # #
    # # for i in arr.split():
    # #     array.append(int(i))
    # #
    # # print(array)
    #
    # # if "F" in choice:
    # #     print("File")
    # #     filename = input()
    # #
    # #     if "a" in filename:
    # #         print("Error")
    # #     else:
    # #         usefile = filename
    # #         file = open(usefile, 'r')
    # #         amount = file.readline()
    # #         num = file.readline()
    # #
    # #         # numpy.array(num.split(" "))
    # #         print(numpy.array(num.split(" ")))
    # #     pass
    # #
    # # elif "I" in choice:
    # #     lines = []
    # #
    # #     while True:
    # #         user_input = input()
    # #
    # #         if user_input == '':
    # #             break
    # #         else:
    # #             lines.append(user_input)
    # #
    # #     amount = lines[0]
    # #
    # #     np_array = numpy.empty(amount)
    # #     print('a')
    # #
    # #     for i in lines[1].split():
    # #         np_array.append(int(i))
    # #
    # #     print(np_array)
    # #
    # #     pass
    # #
    # # else:
    # #     print("Error in input choice")
    #
    # # let user input file name to use, don't allow file names with letter a
    # # account for github input inprecision
    #
    # # input number of elements
    # # input values in one variable, separate with space, split these values in an array
    # # call the function and output it's result
    # pass


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
threading.Thread(target=main).start()