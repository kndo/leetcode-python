#!/usr/bin/env python

def max_area(heights):
    """Find the max area made by two heights in a list of heights that span
    the x-axis.

    Time: O(n^2) -- nested loops to compute all possible areas
    Space: O(1) -- just keep track of the max area
    """
    n = len(heights)

    if n < 2:
        return None

    max_val = 0
    for i in range(n):
        h1 = heights[i]
        for j in range(i+1, n):
            h2 = heights[j]
            h = min(h1, h2)
            w = j - i
            area = h * w

            if area > max_val:
                max_val = area

    return max_val


def main():
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ans = 49

    assert max_area(heights) == ans


    corner_cases = [
        ([], None),   # len(heights) == 0
        ([8], None),  # len(heights) == 1
    ]

    for heights, ans in corner_cases:
        assert max_area(heights) == ans


if __name__ == '__main__':
    main()
