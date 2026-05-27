# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

# Example 1:

# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]
# Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

# Example 2:

# Input: nums = [4,5,6], target = 10

# Output: [0,2]

# brute force solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n=len(nums) 

        for i in range(0,n):   # for 0 of i , j runs the entire loop
            for j in range(0,n): # [range -> indices 0 to 4]
                if i!=j and  nums[i]+nums[j]==target:
                    return [i,j]
        return 0

# Time complexity = O(n^2)
# Space complexity = O(1)


# Optimal solution using hashmap

#  Example question : nums=[3,4,5,6] target=7

# diff= target - nums[i]
# target=7 
# 7-3=4 not in hashmap store {nums[i]:index, 3:0}
# Then 7-4=3 is in hashmap and 4+3=7 return [0,1] 

#Use hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited={}

        for i in range(len(nums)):
            diff= target-nums[i]

            if diff not in visited:
                visited[nums[i]]=i
            else
              return [visited[diff],i]

# Time complexity = O(n)
# Space complexity = O(n)