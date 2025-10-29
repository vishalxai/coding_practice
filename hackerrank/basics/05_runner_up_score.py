"""
Problem: Find the Runner-Up Score!
Source: HackerRank - Python (Basic)
Level: Easy
Date: 2025-10-27
Description:
    Given the participants' scores, find the runner-up score.
    The runner-up is the second highest distinct score.

Input Format:
    The first line contains an integer n (number of scores).
    The second line contains n space-separated integers.

Output Format:
    Print the runner-up score.

Example Input:
    5
    2 3 6 6 5

Example Output:
    5
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    # Remove duplicates using a set, then convert back to a list
    unique_scores = list(set(arr))

    # Sort the list in ascending order
    unique_scores.sort()

    # The second largest element is at index -2
    runner_up = unique_scores[-2]
    print(runner_up)