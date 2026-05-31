#                                     //Contains Duplicate


# // Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# // Example 1:

# // Input: nums = [1, 2, 3, 3]

# // Output: true

# // Example 2:

# // Input: nums = [1, 2, 3, 4]

# // Output: false


# The output is correct but the solution is O(n) and problematic if the array isn't sorted
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
      n = len(nums)

      for i in range(0,n-1):
           if nums[i]==nums[i+1]:
              return True

      return False   


#Using the set() -> Only one value is allowed at a time:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

    class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
      seen = set()

      for num in nums:
        if num in seen:
          return True
        seen.add(num)
      
      return False

# Time Complexity = O(n)
# Space Complexity = O(n)


# Dry run

# num = [1,2,3,3]
# seen = {}

# seen = {1}
# seen = {1,2}
# seen={1,2,3}
# then num=3, num is in seen; the set doesn't store the duplicate values
# So, returns True and the function exists.



# Using the sort function: 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
      nums.sort() #O(nlogn)
      n=len(nums)
      
      for i in range(0,n-1): # O(n)
        if nums[i]==nums[i+1]:
          return True
      return False


#Time complexity total = O(nlogn) + O(n)
# So, time complexity = O(nlogn)
#Space complexity = O(1)


#So, the best solution to this problem  is using hashing because it has O(n) time complexity and
#Range of time complexity is:
#O(c)< O(log logn) < O(logn) < O(n^1/2) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(n^k) < O(2^n) < O(n^n) < O(2^2^n)

