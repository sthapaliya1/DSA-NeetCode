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
                    return [i+1,j+1]
        return 0

# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Solution using the hashmap :



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(numbers)):
             diff = target - numbers[i] 

             if diff not in seen:
                seen[numbers[i]]= i
             else:
                return [seen[diff] + 1, i + 1]

#Time complexity =  O(n)
#Space complexity = O(n)

# Optimal solution: Two pointer technique

        left = 0
        right = len(numbers) - 1

        while left<right:

            total = numbers[left] + numbers[right]

            if total < target:
               left += 1
            elif total > target:
                right -= 1
            else:
                return [left+1, right+1]


# Time Complexity = O(n)
# Space complexity = O(1)