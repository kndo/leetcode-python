#!/usr/bin/env python

def rotate1(nums, k):
    """Rotate an array to the right by k steps, where k is non-negative."""

    if k == 0:
        return nums

    n = len(nums)
    new_nums = [0] * n

    for i in range(n):
        j = (i + k) % n  # Use modulo for wrap-around
        new_nums[j] = nums[i]

    return new_nums


# def rotate2(nums, k):
#     """Rotate an array to the right by k steps, where k is non-negative."""
#     pass


# def rotate2(nums, k):
#     """Rotate an array to the right by k steps, where k is non-negative."""
#     pass


def main():
    # Example 1
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    assert rotate1(nums, k) == [5, 6, 7, 1, 2, 3, 4]
    # assert rotate2(nums, k) == [5, 6, 7, 1, 2, 3, 4]
    # assert rotate3(nums, k) == [5, 6, 7, 1, 2, 3, 4]


    # Example 2
    nums = [-1, -100, 3, 99]
    k = 2

    assert rotate1(nums, k) == [3, 99, -1, -100]
    # assert rotate2(nums, k) == [3, 99, -1, -100]
    # assert rotate3(nums, k) == [3, 99, -1, -100]


if __name__ == '__main__':
    main()
