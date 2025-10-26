"""
Problem: Print Function
Source: HackerRank - Python
Level: Easy
Date: 2025-10-23
Description:
    Given an integer n, print all numbers from 1 to n without spaces.
"""

if __name__ == '__main__':
    n = int(input())
    print(*range(1,n+1),sep='')