#!/usr/bin/env python3
"""A module that solves the lockboxes problem"""


def canUnlockAll(boxes):
    """Function that determines if all the boxes can be opened"""
    num_boxes = len(boxes)  # Total number of boxes
    visited = [False] * num_boxes  # Keeps track of visited boxes
    visited[0] = True  # Mark the first box as visited
    stack = [0]  # Stack for DFS traversal

    while stack:
        current_box = stack.pop()

        # Explore the keys in the current box
        for key in boxes[current_box]:
            if key < num_boxes and not visited[key]:
                visited[key] = True
                stack.append(key)

    # Check if all boxes have been visited
    return all(visited)
