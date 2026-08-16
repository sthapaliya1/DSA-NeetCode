# Permutation in String

# You are given two strings s1 and s2.

#  Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true

# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".


# Example 2:
    
# Input: s1 = "abc", s2 = "lecaabee"

# Output: false


# The solution:

# Store the frequency of the characters in s1:
#    counter = [0] * 26
#    index = ord(s[j]) - ord('a')
#    counter[index]+=1 // for storing character and frequency of s1

#  Search s1 permutation in s2:
#    window-based approach
   
# Maintain the freqcount of both and sliding window, compare freq of s1 in s2:


class Solution:

    def isFreq(self, freq1, freq2):
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False

        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:

        counter=[0]*26
        for i in range(len(s1)):
            index=ord(s1[i])-ord('a')
            counter[index]+=1

            window_size=len(s1)
            
        for i in range(len(s2)):
            windIndex=0
            index=i
            counter_windFreq=[0]*26

            while windIndex < window_size and index < len(s2):
                index1=ord(s2[index])-ord('a')
                counter_windFreq[index1]+=1
                windIndex+=1
                index+=1
        
                if(self.isFreq(counter,counter_windFreq)):
                    return True
        return False
        
        
# Time complexity = O(n^2)
# Space complexity = O(1)

