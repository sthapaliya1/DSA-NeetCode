# You are given an array of non-negative integers height which represent 
# an elevation map. Each value height[i] represents the height of a bar, w
# hich has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:
    
#     Input: height = [0,2,0,3,1,0,1,3,2,1]

#     Output: 9


# Brute force solution:

class Solution:
    def trap(self, height: List[int]) -> int:

# min(lmax,rmax)-height[i]

      amount=0

      n=len(height)

      for i in range(0,n):
        lmax=0
        rmax=0

        for j in range(0,n):
            if i>=j:
                lmax=max(lmax,height[j])
            if i<=j:
                rmax=max(rmax,height[j])
        amount+=min(lmax,rmax)-height[i]
      return amount
        
               
# Time complexity = O(n^2)
# Space complexity = O(1)



# Better solution:


# using the prefix and suffix of lmax and rmax:

n=len(height)
lmax=[0]*n
rmax=[0]*n
ans=0

lmax[0]=0
rmax[n-1]=1

for i in range(1,n):
  lmax[i]=max(lmax[i-1],height[i])
for i in range(n-2,-1,-1):
  rmax[i]=max(rmax[i+1],height[i])
for i in range(0,n):
   ans+=min(lmax[i],rmax[i])-height[i]
return ans


# Time complexity = O(n)
# Space complexity = O(n)



# Optimal solution:

n=len(height)
ans=0
lmax= 0
rmax= 0
lp=0
rp=n-1

while lp<rp:
    lmax=max(lmax,height[lp])
    rmax=max(rmax,height[rp])

    if lmax<rmax:
        ans+=lmax-height[lp]
        lp+=1
    else:
        ans+=rmax-height[rp]
        rp-=1
return ans

# Time complexity = O(n)
# Space complexity = O(1)