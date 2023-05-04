def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True  # first box is always unlocked
    stack = [0]  # start with first box

    while stack:
        box_num = stack.pop()
        for key in boxes[box_num]:
            if key >= num_boxes:  # invalid key
                continue
            if not unlocked_boxes[key]:
                unlocked_boxes[key] = True
                stack.append(key)

    return all(unlocked_boxes)
