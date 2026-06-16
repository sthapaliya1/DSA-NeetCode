# Longest Consecutive Sequence
# Medium
# Topics
# Company Tags
# Hints
# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [2,20,4,10,3,4,5]

# Output: 4
# Explanation: The longest consecutive sequence is [2, 3, 4, 5].

# Example 2:

# Input: nums = [0,3,2,5,4,6,1,1]

# Output: 7


# The optimal solution:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     
        n = len(nums)

        if n == 0:
            return 0

        visited = set()
        longest = 1

        # Add all numbers to set
        for num in nums:
            visited.add(num)

        # Loop through the set
        for it in visited:
            if it - 1 not in visited:
                cnt = 1
                x = it

                while x + 1 in visited:
                    x = x + 1
                    cnt += 1

                longest = max(cnt, longest)
        return longest

# Time complexity : O(n)
# Space complexity: O(n)


# Shorter version:

  visited = set(nums)
        longest = 0

        for it in visited:
            if it - 1 not in visited:
                cnt = 1
                x = it

                while x + 1 in visited:
                    x += 1
                    cnt += 1

                longest = max(longest, cnt)

        return longest


# The better solution using sort:
        nums.sort()
        n=len(nums)

        cnt=1
        last_smaller=nums[0]
        longest=1

        

        for i in range(0,n):
            if nums[i]-1 == last_smaller:
                cnt=cnt+1
                last_smaller=nums[i]

            elif nums[i]!=last_smaller:
                cnt=1
                last_smaller=nums[i]

            longest=max(longest,cnt)

        return longest





    # The Brute force solution:
    class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     
        n = len(nums)

        if n == 0:
            return 0

        def ls(arr, num):
            for i in range(n):
                if arr[i] == num:
                    return True
            return False

        longest = 1

        for i in range(n):

            x = nums[i]
            cnt = 1

            while ls(nums, x + 1):
                x += 1
                cnt += 1

            longest = max(longest, cnt)

        return longest