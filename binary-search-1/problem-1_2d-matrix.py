# https://leetcode.com/problems/search-a-2d-matrix/
# Solution Date: 30 Sept 2023

from typing import List


# Solution A: Brute Force
# Time: O(n*m)
# Space: O(1)
def search_matrix_a(matrix: List[List[int]], target: int) -> bool:
    for row in matrix:
        for num in row:
            if num == target:
                return True
    return False


# Solution B: Binary Search on each row
# Time: O(n*log(m))
# Space: O(1)


def search_matrix_b(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    n = len(matrix[0])
    for row in matrix:
        if binary_search(row, n, target):
            return True

    return False


# Solution C: First find row by Binary Search + Binary Search for row
# Time: O(log(n) + log(m)) = O(log(n*m))
# Space: O(1)


def search_matrix_c(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m = len(matrix)
    n = len(matrix[0])

    # Binary search for row
    top_pointer, bottom_pointer = 0, m - 1
    while top_pointer <= bottom_pointer:
        mid = (top_pointer + bottom_pointer) // 2

        if matrix[mid][0] == target:
            return True

        elif matrix[mid][0] < target:
            # Check for next row if exists
            if mid + 1 == m or (mid + 1 < m and matrix[mid + 1][0] > target):
                return binary_search(matrix[mid], n, target)

            # Target can not be in current row
            top_pointer = mid + 1

        else:
            bottom_pointer = mid - 1

    return False


def binary_search(array, n, target):
    left_pointer = 0
    right_pointer = n - 1

    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2
        current_element = array[mid]

        if target == current_element:
            return True

        if target < current_element:
            right_pointer = mid - 1
        else:  # target > current_element
            left_pointer = mid + 1

    return False


# Tests
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

# assert search_matrix_c(matrix, 13) == False
# assert search_matrix_c(matrix, 11) == True
# assert search_matrix_c(matrix, 3) == True
# assert search_matrix_c([[1]], 3) == False
# assert search_matrix_c([[1, 3]], 3) == True
