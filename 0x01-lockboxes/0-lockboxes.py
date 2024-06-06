#!/usr/bin/python3
"""The script contains the function lockboxes"""


def canUnlockAll(boxes):
    """Returns true if all boxes are unlocked"""

    n = len(boxes)
    unlock_boxes = [False] * n
    unlock_boxes[0] = True

    keys = boxes[0]

    while keys:
        new_keys = []
        for key in keys:
            if key < n and not unlock_boxes[key]:
                unlock_boxes[key] = True
                new_keys.extend(boxes[key])

        keys = new_keys

    return all(unlock_boxes)
