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

  # Edge case:
        # If array is empty, there is no sequence
        if n == 0:
            return 0

        # Stores the longest consecutive sequence found so far
        longest = 1

        # Create a set for O(1) lookup
        st = set()

        # Insert all numbers into the set
        for i in range(n):
            st.add(nums[i])

        # Traverse every unique element
        for it in st:

            # Check whether 'it' is the start of a sequence
            # Example:
            # 1,2,3,4
            # For 1 -> 0 not present => start
            # For 2 -> 1 present => not start
            if it - 1 not in st:

                # Current sequence length
                cnt = 1

                # Current number
                x = it

                # Keep moving forward while next number exists
                while x + 1 in st:  # every num is visited only once in the loop
                    x = x + 1
                    cnt = cnt + 1

                # Update longest sequence length
                longest = max(longest, cnt)

        return longest

# Time complexity : O(n)
# Space complexity: O(n)