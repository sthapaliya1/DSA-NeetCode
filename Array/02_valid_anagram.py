# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false



# Anagram is a string which contains exact same characters as another string.

# So, comparing there are ways to solve this problem : 


# STEPS:
    # The length of the string should be same 
    # After comparing the length the char inside the strings should also be same:


# Brute force solution:


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

    if len(s)!=len(t)
      return False

    
    t_list=list(t)   # Space complexity = O(n) : (if no list had been created then it would be O(1))

    for char in s:  # -> O(n)
        found=False


        for i in range(len(t_list)): # -> O(n)
            if t_list[i]==char:
                found=True
                t_list.pop(i)
                break
        if found==False:
            return False

    return True

# Time Complexity of this solution = O(n^2)
# Space complexity : O(n)


# More optimized solution : use of sorting

# First sort and then compare

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

    t_sorted=sorted(t)
    s_sorted=sorted(s)

    if t_sorted==m_sorted:
        return True
    else:
        return False

    OR 

    return sorted(t)==sorted(s)

    #Time complexity = O(nlogn) -> due to sorting algo  O(n)<O(nlogn)<O(n^2)
    #Space complexity = O(n),  -> comparing two sorted list

    # If sort() was used then space complexity would have been O(1) because it is used for list and modifies the list 
    # doesn't create a complete new list

    # sorted(s) function  creates a complet new sorted list than modified used for strings, list, tuples, sets
    # Space complexity is O(n)


# Most optimized solution : Use of dictionary/hashmaps and count the frequency


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

    if len(s)!=len(t):
      return False
    
    S, T = {}, {}


    # Populates the hashmap
    for i in range(len(s)):  #-> O(n)
        S[s[i]]= 1 + S.get(s[i],0)  #gets the count of the characters
        T(t[i])= 1 + T.get(t[i],0)  # gets the count of the characters

    # Compares the count of characters in both of them
    for char in s:   #-> O(n)
        if S[char]!=T.get(char,0):  # get the count of characters if not found fill it to 0
            return False
    return True
    
    # Time Complexity = O(n) 
    # Space Complexity = O(n)

    
        




