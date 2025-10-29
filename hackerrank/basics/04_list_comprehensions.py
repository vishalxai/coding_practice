"""
Problem: List Comprehensions
Source: HackerRank - Python (Basic Data Types)
Level: Easy
Date: 2025-10-27
Description:
    Given integers x, y, z and n, print a list of all coordinates [i, j, k]
    on a 3D grid where 0 <= i <= x, 0 <= j <= y, 0 <= k <= z and
    i + j + k != n.
    Use list comprehensions instead of multiple loops.

Input Format:
    Four integers x, y, z, n each on a separate line.

Output Format:
    Print the list of coordinates in lexicographic increasing order.

Example Input:
    1
    1
    2
    3

Example Output:
    [[0, 0, 0], [0, 0, 1], [0, 0, 2],
     [0, 1, 0], [0, 1, 1],
     [1, 0, 0], [1, 0, 1],
     [1, 1, 0], [1, 1, 2]]
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Generate all [i, j, k] combinations using list comprehension
    # Keep only those where i + j + k != n
    coords = [[i, j, k]
              for i in range(x + 1)
              for j in range(y + 1)
              for k in range(z + 1)
              if i + j + k != n]

    print(coords)