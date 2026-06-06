# Two Integer Sum II

# Given an array of integers numbers that is sorted in non-decreasing order.

# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

# There will always be exactly one valid solution.

# Your solution must use 
# O(1)
# O(1) additional space.

# Example 1:

# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]


# A non-decreasing order because each element is greater than or equal to the previous one.

# Brute force solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n=len(numbers)

        for i in range(0,n):
            for j in range(0,n):
                if numbers[i]+numbers[j]==target and i!=j:
                    return [numbers[i],numbers[j]]
        return 0

# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Solution using the hashmap :
