# alx interview questions (stacks)
# !/usr/bin/python3


def canUnlockAll(boxes):
    """ a function that determines if all boxes can be opened """
    stack = {}
    waitList = []

    for i in range(len(boxes)):
        if i not in stack and i != 0:
            waitList.append(i)
        for j in range(len(boxes[i])):
            if boxes[i][j] not in stack:
                stack.update({boxes[i][j]: i})
    if waitList:
        for k in waitList:
            if k not in stack:
                return False
        return True
    else:
        return True
