# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
     ans=[]
     S={}

     for num in nums:   #O(n)
        if num not in S:
            S[num] = 1
        else:
            S[num]+=1

     for key,val in S.items(): # O(m)   
        if len(ans)<k:
            heapq.heappush(ans, [val,key])  # O(logk)
        else:
            heapq.heappushpop(ans,[val,key])
     return [key for value, key in ans] # O(k)
        
# Time Complexity is O(n)+ O(mlogk)+ O(k)
# Space Complexity:

# O(m) for the frequency dictionary,
# O(k) for the min-heap storing the top k elements,  //both the heap and list can contain at most k elements
# and O(k) for the returned list.

# Therefore:

# O(m + k)

