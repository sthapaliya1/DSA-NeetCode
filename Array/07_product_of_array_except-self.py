# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res=[]

        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i!=j:
                   product *= nums[j]
                
            res.append(product)
        return res

Time Complexity : O(n^2)
Space Complexity : O(n)


#Optimal solution:

# nums = [1,2,3,4]
# Ans : [24, 12, 8, 6]

#   left_product / prefix  ---i ---- right_product/ suffix

# return (left_product * right_product)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        res = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res

# Time complexity: O(n)
# Space complexity: O(n)