#!/usr/bin/env python

def two_sum1(nums, target):
    """Find indexes i and j of an array whose values add up to the target.
    Can assume that each input has exactly one solution.

    Time: O(n^2) -- nested loops to find all combinations of sums
    Space: O(1) -- loop through the array in place; each sum is O(1)
    """
    if len(nums) < 2:
        return [None, None]

    for i, u in enumerate(nums):
        for j, v in enumerate(nums):
            if u + v == target:
                return [i, j]

    return [None, None]


def two_sum2(nums, target):
    """Find indexes i and j of an array whose values add up to the target.
    Can assume that each input has exactly one solution.

    Time: O(n) -- loop through the array once; past dict get/set is O(1)
    Space: O(n) -- might have to store all n elements in past dict
    """
    if len(nums) < 2:
        return [None, None]

    past = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in past:
            return [past[diff], i]
        past[nums[i]] = i

    return [None, None]


def two_sum3(nums, target):
    """Find indexes i and j of an array whose values add up to the target.
    Can assume that each input has exactly one solution.

    nums *must* be sorted

    Time: O(n) -- might have to traverse to the middle indexes of the array
    Space: O(1) -- traverse the array in place; each sum is O(1)
    """
    if len(nums) < 2:
        return [None, None]

    l, r = 0, len(nums) - 1
    while nums[l] < nums[r]:
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1

    return [None, None]


def main():
    nums = [2, 7, 11, 15]
    target = 9
    ans = [0, 1]

    assert two_sum1(nums, target) == ans
    assert two_sum2(nums, target) == ans
    assert two_sum3(nums, target) == ans


    short_circuit_cases = [
        ([], 3),   # len(nums) == 0
        ([1], 8),  # len(nums) == 1
    ]

    for nums, target in short_circuit_cases:
        assert two_sum1(nums, target) == [None, None]
        assert two_sum2(nums, target) == [None, None]
        assert two_sum3(nums, target) == [None, None]


    interesting_cases = [
        ([2, 7, 11, 15], 99, [None, None]),  # No matches found
    ]

    for nums, target, ans in interesting_cases:
        assert two_sum1(nums, target) == ans
        assert two_sum2(nums, target) == ans
        assert two_sum3(nums, target) == ans


if __name__ == '__main__':
    main()
