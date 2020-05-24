#!/usr/bin/env python

def people_indexes(favorite_companies):
    """Return the indices of people whose list of favorite companies is not a
    subset of any other list of favorite companies.

    Time: O(n^2) -- nested loops to compare current list with all other lists
    Space: O(n) -- all lists may be disjoint with one another
    """
    n = len(favorite_companies)
    elim_indexes = set()

    for i in range(n):
        for j in range(i+1, n):
            u = set(favorite_companies[i])
            v = set(favorite_companies[j])
            if u.issubset(v):
                elim_indexes.add(i)
            if v.issubset(u):
                elim_indexes.add(j)

    all_indexes = set(range(n))
    return list(all_indexes - elim_indexes)


def main():
    example_cases = [
        # Example 1
        (
            [
                ['leetcode', 'google', 'facebook'],
                ['google', 'microsoft'],
                ['google', 'facebook'],
                ['google'],
                ['amazon'],
            ],
            [0, 1, 4]
        ),
        # Example 2
        (
            [
                ['leetcode', 'google', 'facebook'],
                ['leetcode', 'amazon'],
                ['facebook', 'google'],
            ],
            [0, 1]
        ),
        # Example 3
        (
            [
                ['leetcode'],
                ['google'],
                ['facebook'],
                ['amazon'],
            ],
            [0, 1, 2, 3]
        ),

    ]

    for favorite_companies, ans in example_cases:
        assert people_indexes(favorite_companies) == ans


    corner_cases = [
        (
            [],            # len(favorite_companies) == 0
            []
        ),
        (
            [['google']],  # len(favorite_companies) == 1
            [0]
        ),
    ]

    for favorite_companies, ans in corner_cases:
        assert people_indexes(favorite_companies) == ans


if __name__ == '__main__':
    main()
