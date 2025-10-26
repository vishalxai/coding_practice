"""
Problem: Maximize It!
Source: HackerRank - Python / itertools
Level: Medium
Date: 2025-10-23
Description:
    You are given K lists and an integer M.
    Your task is to select one element from each list such that the value of:
        S = (x1^2 + x2^2 + ... + xk^2) % M
    is maximized.

Input Format:
    The first line contains two space-separated integers K and M.
    The next K lines each contain an integer Ni followed by Ni elements.

Output Format:
    Output a single integer, the maximum possible value of S.

Example Input:
    3 1000
    2 5 4
    3 7 8 9
    5 5 7 8 9 10

Example Output:
    206
"""

from itertools import product

if __name__ == '__main__':
    K, M = map(int, input().split())
    lists = []

    for _ in range(K):
        data = list(map(int, input().split()))
        lists.append(data[1:])  # skip the first number (count)

    max_val = 0

    for combo in product(*lists):
        total = (sum(x**2 for x in combo)) % M
        if total > max_val:
            max_val = total

    print(max_val)

