#             Valid palindrome

# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.


# Palindrome reads same forward and backward
# So , the reversed string and the actual string should be same and in question it is stated as it ignores all the alphanumeric characters.
# So we use .isalnum() -> a function that return True if there are no symbols in the string and False if there are symbols in the string

# Brute force solution:
#  1. Check if there are any alpha numeric characters
#  2. If there are alphanumeric characters, then don't compare
#  3. While comparing do not consider the upper case letters change it into the lowercase
#  4. Compare at the end with the reverse string



class Solution:
    def isPalindrome(self, s: str) -> bool:

    cleaned=""  #-> O(n) space complexity

    for char in s:  # O(n) -> time complexity
        if char.isalnum():
            cleaned+=char.lower()

    return cleaned==cleaned[::-1]  # Compares with the reverse string

# Time Complexity : O(n)
# Space Complexity : O(n)


# Optimal solution and better approach
# Two pointer technique
# Where the left and right are listed , left at the leftmost index and right at the rightmost index which is len(right)-1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
         left = 0
         right= len(s)-1


         while left < right:  # O(n)

            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            elif s[left].lower()!=s[right].lower():
                return False
            else:
               left+=1
               right-=1

         return True

#Time complexity: O(n)
#Space complexity: O(1) # No extra data structures used ...