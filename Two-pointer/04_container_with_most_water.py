# You are given an integer array heights where heights[i] represents the height of the 
# ith bar.

# You may choose any two bars to form a container. Return the maximum amount of water
# a container can store

# Example 1:
# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36

# Example 2:
# Input: height = [2,2,2]
# Output: 4


# Usually, the water container is max when first to last bar.
# however if first bar is taller more water can be stored

# Brute force solution

class Solution:
def maxArea(self, heights: List[int]) -> int:
        maxwater=0

        for i in range(0,len(heights)):
            for j in range(i+1,len(heights)):
                width= j-i
                height= min(heights[i],heights[j])
                currentwater = width * height
            maxwater= max(currentwater, maxwater)
        return maxwater

# Time complexity = O(n^2)
# Space complexity = O(1)



# The optimal solution:

def maxArea(self, heights: List[int]) -> int:
        maxwater=0

        lp = 0
        rp = len(heights) - 1

        while lp < rp:
            width = rp - lp
            height = min(heights[lp], heights[rp])
            currwater = width * height
            maxwater = max(maxwater, currwater)

            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1

        return maxwater

# Time complexity = O(n)
# Space complexity = O(1)
