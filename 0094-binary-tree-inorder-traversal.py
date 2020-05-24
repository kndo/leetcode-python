#!/usr/bin/env python

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(node):
    """Perform inorder traversal of the subtree at the given tree node.
    Inorder traversal visits the left subtree, root, then right subtree.

    Use a stack, which has last-in, first-out behavior, to traverse leftward
    and push root then left subtree, and then in reverse pop left subtree then
    root to our result.

    Reference: https://github.com/joowani/binarytree
    """
    result = []
    node_stack = []

    while True:
        if node is not None:
            node_stack.append(node)
            node = node.left
        elif len(node_stack) > 0:
            node = node_stack.pop()
            result.append(node.val)
            node = node.right
        else:
            break

    return result


def main():
    # Input: [1, None, 2, 3]
    root = Node(1)
    root.right = Node(2)
    root.right.left = Node(3)
    ans = [1, 3, 2]

    assert inorder_traversal(root) == ans


if __name__ == '__main__':
    main()
