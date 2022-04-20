#!/usr/bin/python3

"""
Task Holberton-Lockboxes
"""


def canUnlockAll(boxes):
    """
    CanUnlockALl
    """
    if len(boxes) <= 1:
        return True
    pend = [0]
    vista = set(pend)

    while pend:
        current = pend.pop()
        for key in boxes[current]:
            if key not in vista and key < len(boxes):
                pend.append(key)
                vista.add(key)
    return len(vista) == len(boxes)
