# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

# Example 1:

# Input: nums = [1,2,1,0,4,2,6], k = 3

# Output: [2,2,4,4,6]



# Brute force solution use loops:


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result=[]
        n=len(nums)

        for i in range(0,n-k+1):
            maximum=nums[i]
            
            for j in range(i,i+k):
                if nums[j]>maximum:
                   maximum=nums[j]
            result.append(maximum)
        return result
    
    
    
    
# The optimized solution:

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq=deque()
        result=[]

        # Build the first window:
        for i in range(k):

            # Remove the smaller element from the back:
            while len(dq)>0 and nums[dq[-1]]<=nums[i]:
                dq.pop()
            dq.append(i)

            # process remaining windows:
        for i in range(k,len(nums)):

                # maximum of previous window
            result.append(nums[dq[0]])

            # remove the index that is no longer inside window
            while len(dq)>0 and dq[0]<=i-k:
                dq.popleft()

                #Remove the smaller element from back:
            while len(dq)>0 and nums[dq[-1]]<=nums[i]:
                dq.pop()
                # add the current index:
            dq.append(i)
        result.append(nums[dq[0]])
        return result






