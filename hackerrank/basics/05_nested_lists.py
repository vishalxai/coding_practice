"""
07_nested_lists.py
Problem: Nested Lists (HackerRank)
Description:
    Given names and grades for N students, print the name(s) of student(s)
    having the second lowest grade. If there are multiple, print names
    in alphabetical order, each on a new line.

Input:
    First line: integer N
    Next 2N lines: name (string) then grade (float)

Example:
    Input:
        5
        Harry
        37.21
        Berry
        37.21
        Tina
        37.2
        Akriti
        41
        Harsh
        39
    Output:
        Berry
        Harry
"""

if __name__ == "__main__":
    # Read number of students
    n = int(input().strip())

    # Collect [name, grade] pairs
    students = []
    for _ in range(n):
        name = input().strip()
        grade = float(input().strip())
        students.append([name, grade])

    # Extract distinct grades (set removes duplicates) and sort ascending
    distinct_grades = sorted({grade for _, grade in students})

    # Second lowest distinct grade (problem guarantees at least two distinct)
    second_lowest = distinct_grades[1]

    # Collect names with that grade, sort alphabetically, and print
    result_names = sorted([name for name, grade in students if grade == second_lowest])
    for name in result_names:
        print(name)