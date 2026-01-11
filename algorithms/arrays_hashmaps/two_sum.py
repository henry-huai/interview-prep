"""
Two Sum

Given an array of integers and a target value, return the indices
of the two numbers that add up to the target.

This implementation prioritizes clarity, correctness, and
explainability over clever tricks.
"""

"""
Time complexity: O(n^2)

Space complexity: O(n) (peak extra memory due to the largest slice)
"""
def two_sum(numbers : list[int], target: int) -> bool:
    for i in range(len(numbers)):
        remaining = target - numbers[i]
        if remaining in numbers[i+1:]:
            return True
    return False


