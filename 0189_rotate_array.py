#!/usr/bin/env python

def rotate1(nums, k):
    """Rotate an array to the right by k steps, where k is non-negative.

    Time: O(n) -- set n elements in new array
    Space: O(n) -- create a new array to store the rotated elements
    """
    n = len(nums)

    if k == 0:
        return nums
    if n < 2:
        return nums

    k = k % n  # In case k > len(nums), prevent redundant rotations

    new_nums = [0] * n

    for i in range(n):
        j = (i + k) % n  # Use modulo for wrap-around
        new_nums[j] = nums[i]

    return new_nums


def rotate2(nums, k):
    """Rotate an array to the right by k steps, where k is non-negative.

    Time: O(kn) -- rotate n elements k times
    Space: O(1) -- rotate elements in place using a holder variable
    """
    n = len(nums)

    if k == 0:
        return nums
    if n < 2:
        return nums

    k = k % n  # In case k > len(nums), prevent redundant rotations

    for _ in range(k):
        last = nums[n-1]  # The extra O(1) space
        for i in range(n):
            # Since we're rotating elements to the right, we should traverse the
            # index from right-to-left to avoid overwriting previously traversed
            # elements
            j = n - 1 - i
            if j != 0:
                nums[j] = nums[j-1]
            else:
                nums[j] = last

    return nums


def rotate3(nums, k):
    """Rotate an array to the right by k steps, where k is non-negative.

    Time: O(k(n-k)) => O(kn - k^2) -- rotate (n-k) elements k times
    Space: O(1) -- rotate elements in place using a holder variable
    """
    n = len(nums)

    if k == 0:
        return nums
    if n < 2:
        return nums

    k = k % n  # In case k > len(nums), prevent redundant rotations

    for i in range(k):
        saved = nums[n - k + i]  # The extra O(1) space
        for j in range(n - k + i, i, -1):
            # Since we're rotating elements to the right, we should traverse the
            # index from right-to-left to avoid overwriting previously traversed
            # elements
            nums[j] = nums[j-1]
        nums[i] = saved

    return nums


def main():
    example_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),  # Example 1
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),          # Example 2
    ]

    for nums, k, ans in example_cases:
        assert rotate1(nums, k) == ans
        assert rotate2(list(nums), k) == ans
        assert rotate3(list(nums), k) == ans


    # Short-circuit cases
    short_circuit_cases = [
        ([1, 2, 3], 0),  # k = 0
        ([], 3),         # len(nums) = 0
        ([1], 2),        # len(nums) = 1
    ]

    for nums, k in short_circuit_cases:
        assert rotate1(nums, k) == nums
        assert rotate2(nums, k) == nums
        assert rotate3(nums, k) == nums


    # Interesting cases
    interesting_cases = [
        ([1, 2, 3, 4], 10, [3, 4, 1, 2])  # k > len(nums)
    ]

    for nums, k, ans in interesting_cases:
        assert rotate1(nums, k) == ans
        assert rotate2(list(nums), k) == ans
        assert rotate3(list(nums), k) == ans


if __name__ == '__main__':
    main()
