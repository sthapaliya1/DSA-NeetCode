# Longest Repeating Character Replacement


# You are given a string s consisting of only uppercase english characters and an integer k.
# You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains 
# only one distinct character.

# Example 1:  Input: s = "XYYX", k = 2
# Output: 4

# Example 2: Input: s = "AAABABB", k = 1
# Output: 5

# Steps : Maintain the hashmap to store the character and the frequency, maxfrequency.
# Update the max_len and return the max_len:

    #  length - max_frequency <= k 
    #    where, length - max_frequency is no of characters that can be replaced.


# Brute force solution:

n=len(s)
max_len=0
for i in range(0,n):
    max_freq=0
    count=[0]*26
    
    for j in range(i,n):
        index = ord(s[j])-ord('A')
        count[index]+=1
        
        max_freq=max(max_freq,count[index])
        change=(j-i+1) - max_freq
        
        if (change <= k):
            max_len=max(max_len,(j-i+1))
        else:
            break
    return max_len

# Time Complexity = O(n^2)
# Space Complexity = O(1)




# The optimal solution:

n=len(s)
l=0
r=0
max_len=0
max_freq=0
count=[0]*26

while(r<len(s)):
    index=ord(s[r])-ord('A')
    count[index]+=1
    
    max_freq = max(max_freq,count[index])
    change= (r-l+1) - max_freq
    
    if (change > k)
    {
        index=ord(s[l])-ord('A')
        count[index]-=1
        l+=1
    }
    
    max_len= max(max_len, (r-l+1))
return max_len

        

