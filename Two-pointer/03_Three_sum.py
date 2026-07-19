
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].

# Example 2:

# Input: nums = [0,1,1]

# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:

# Input: nums = [0,0,0]

# Output: [[0,0,0]]



# Brute force solution:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Because the output should not contain the duplicate triplets:
        output=set()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if i!=j and j!=k and i!=k and nums[i]+nums[j]+nums[k]==0:
                            triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                            output.add(triplet)

        return [list(t) for t in output]
        
# Time complexity = O(n^3) 
# Space complexity = O(m) -> m is no of unique triplets


# Better solution:

 # array[k] = - (array[i] + array[j])

 # [-1,0,1,2,-1,-4] i is fixed , create a set:

 
   output= set()
   n = len(nums)

    for i in range(0,n):
        hashset=set()
        for j in range(i+1,n):
            third = -(nums[i]+nums[j])
            if third in hashset:
                triplet = tuple(sorted([nums[i],nums[j],third]))
                output.add(triplet)
            hashset.add(nums[j])
    return [list(t) for t in output]


# Time complexity = O(n^2)
# Space complexity = O(n+m) { m= no of unique elements}



# The optimized solution:

 [-4, -1, -1, 0, 1, 2]


  ans=[]
  nums.sort()
  n=len(nums)

  for i in range(n):
        if i > 0 and nums[i]==nums[i-1]:
            continue
        j=i+1
        k=n-1

        while j<k:
            total=nums[i]+nums[j]+nums[k]

            if total>0:
                k-=1
            elif total<0:
                j+=1
            else:
                triplet=[nums[i],nums[j],nums[k]]
                ans.append(triplet)
                j+=1
                k-=1

                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1
        return ans 

# (No use of extra data structures)
# Time complexity =  O(nlogn) + O(n^2) 
# Space complexity = O(m) where m is no of unique elements




















# Optimized solution: Using two pointer solution:

        nums.sort()
        output = []

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    output.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return output