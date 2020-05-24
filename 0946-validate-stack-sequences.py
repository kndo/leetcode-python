#!/usr/bin/env python

class Stack:
    def __init__(self):
        self._data = []

    def push(self, e):
        self._data.append(e)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise IndexError('Pop from empty stack')
        return self._data.pop()


def validate_stack_sequences(pushed, popped):
    """Validate if two sequences, pushed and popped, are valid push and pop
    operations on an initially empty stack.

    Time: O(2n) -- push n values, pop n values
    Space: O(n) -- might push all n values to the stack before any popping occurs
    """
    S = Stack()
    i = 0

    for e in popped:
        while i <= len(pushed):
            if not S.is_empty() and S.top() == e:
                S.pop()
                break
            elif i == len(pushed):
                break
            else:
                S.push(pushed[i])
                i += 1

    if S.is_empty():
        return True
    return False


def main():
    example_cases = [
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
    ]

    for pushed, popped, ans in example_cases:
        assert validate_stack_sequences(pushed, popped) == ans


if __name__ == '__main__':
    main()
