# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]


# The output can be in any order....

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
      S= {}  # O(m)

      for num in nums:  # O (n)
        S[num] = S.get(num, 0) + 1

      S = sorted(S.items(), key=lambda x: x[1], reverse=True) # O (m log m)

      return [key for key, value in S[:k]] # runs k times so time complexity is O(k) and returns the new list O(k) space

 # In python to sort in ascending or descending order:
 # sorted(nums)                # ascending
 # sorted(nums, reverse=True)  # descending
             

# Time complexity = O(n)+ O(mlogm) + O(k)= O(n + mlogm)
# Space complexity = O(m) + O(k)   =  k <=m   = O(m)
        
             
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
        
# Time Complexity is O(n)+ O(mlogk)+ O(k) = O(n+ mlogk)
# Space Complexity:

# O(m) for the frequency dictionary,
# O(k) for the min-heap storing the top k elements,  //both the heap and list can contain at most k elements
# and O(k) for the returned list.

# Therefore:

# O(m + k)

