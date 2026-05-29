# Group Anagrams

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]




# Sort the each word
# Create a map in which the sorted word (key) and corresponding list of sorted word is stored
# return the values 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        di={}

        for word in strs:  # O(n)
            sorted_word=tuple(sorted(word))  # sort each word inside  coz the sorted (word) is list and the list is mutuable # O (klogk) sorting for each word
            di[sorted_word] = di.get(sorted_word,[])+[word]  #mapping in the dictionary 
        return list(di.values())  # return the values of the dictionary
        

# The time complexity is O(n* klogk)
# The space complexity is O(n*k)



# Store the letters in the form of ascii value and make it the key and then only store the value with it
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        di={}

        for word in strs: # O(n)
          counter=[0]* 26 
          for char in word: # O(k)
            counter[ord(char)-ord('a')]+=1   #counter adding to the map using ascii
            # substracts the bigger - smaller word
          counter = tuple(counter)
          di[counter]= di.get(counter,[])+ [word]
        return list(di.values())

# The time complexity is O(n* k)
# The space complexity is O(n*k)


# ord(char) = returns the ascii values and then converts the letter into an index from 0 to 25.
# 'a' -> 97 - 97 = 0
# 'b' -> 98 - 97 = 1
# 'c' -> 99 - 97 = 2
# 'z' -> 122 - 97 = 25