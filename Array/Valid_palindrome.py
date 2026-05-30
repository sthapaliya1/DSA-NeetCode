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
#Space complexity: O(1)