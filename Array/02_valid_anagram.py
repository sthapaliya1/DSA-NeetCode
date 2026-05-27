# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
     s1 = sorted(s)
     t2 = sorted(t)

     if s1 == t2:
        return True

     return False

# Time complexity is : O(n log n ) because of sorting





# Using the dictionary --- More optimized solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
     seen={}

    #Condition 1: The length of the string is not same
     if len(s)!=len(t):
       return False

    # To compare the characters use frequency count using dictionary
     for char in s:
        if char in seen:
            seen[char] +=1
        else:
            seen[char]=1
    
     for char in t:
        if char not in seen:
            return False
        
        #If true then check the third condition:
        seen[char] -= 1

        if seen[char]<0:
         return False # as in the jaj case j:0 and further decreasing it leads to -1
   
     return True
# Three conditions:

#Condition 1: If the len of the strings aren't same
#Condition 2: Length and char is same
#Condition 3: Length is same but the char is not:

#Condition 3 example : jar and jaj


# This is more optimized solution than the previous one sorting one
# because the time complexity is O(n) < O(nlogn)

