# Longest Substring Without Repeating Characters


# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.


# Example 1:
    
# Input: s = "zxyzxyz"
# Output: counter char, using set

# counter char

# Brute force solution:

# using the counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

    n=len(s)
    max_len=0
    
    for i in range(0,n):
        counter=[0]*256
       for j in range(i,n):
           index=(ord(s[j]) - ord('a'))
           
           if counter[index]==1:
               break
           counter[index]=1
           length=j-i+1
           max_len=max(max_len,length)
    return max_len

# Time complexity = O(n^2)
# Space complexity = O(1)


# using set:

n=len(s)
max_len=0

for i in range(0,n):
    counter=set()
    for j in range(i,n):
        if s[j] in counter:
            break
        counter.add(s[j])
        length=j-i+1
        max_len=max(max_len,length)
return max_len

#Time complexity = O(n^2)
#Space complexity = O(1)




# Optimal solution:
# Using two pointer and sliding window mechanism:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left=0
        right=0
        max_len=0
        n=len(s)
        S={}
            
        for right in range(len(s)):
            S[s[right]] = 1 + S.get(s[right],0)

            while S[s[right]]>1:
                S[s[left]]-=1
                left+=1
            length=right-left+1
            max_len=max(max_len,length)
        return max_len
    
    # Time complexity = O(n)
    # Space complexity = O(1)
            