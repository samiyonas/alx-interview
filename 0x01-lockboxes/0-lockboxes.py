#!/usr/bin/python3
""" alx interview question (stacks) """


def canUnlockAll(boxes):
    """ a function that determines if all boxes can be opened """
    stack = {}
    waitList = 0

    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            if boxes[i][j] not in stack:
                stack.update({boxes[i][j]: i})
        if i not in stack:
            waitList += 1
    if waitList != 0:
        return False
    else:
        return True

print(canUnlockAll([[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]))
