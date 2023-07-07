#!/usr/bin/python3

def canUnlockAll(boxes):
    total_boxes = len(boxes)
    unlocked_boxes = [False] * total_boxes
    unlocked_boxes[0] = True  # The first box is unlocked by default
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        keys = boxes[current_box]

        for key in keys:
            if key < total_boxes and not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)
