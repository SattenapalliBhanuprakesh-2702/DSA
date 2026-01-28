# Problem — Maximum Subarray Sum (Kadane’s Algorithm)

# Given an integer array nums (can contain positive, negative, and zero), find the maximum possible sum of any non-empty contiguous subarray.

# A subarray must contain at least one element and must be continuous.

# Intuition

# Brute force checks all subarrays → O(n²). Not scalable.

# Key observation:

# A negative running sum will only reduce future sums.

# If the current prefix sum becomes negative, drop it and start fresh from the next element.

# At each index, decide:

# Is it better to extend the previous subarray, or start a new one from here?

# So we track:

# current_sum → best subarray ending at current index

# max_sum → best subarray found so far

# Dynamic decision at every step:

# current_sum = max(nums[i], current_sum + nums[i])
# max_sum = max(max_sum, current_sum)


# This greedy + DP hybrid works because subarray structure has optimal substructure.

# Time & Space Complexity
# Metric	Value
# Time Complexity	O(n) (single pass)
# Space Complexity	O(1) (constant variables)

# This is the optimal solution.

# 1.  [1,2,3,4,5] → 15
# 2.  [5,-2,3,4] → 10
# 3.  [-2,1,-3,4,-1,2,1,-5,4] → 6
# 4.  [7] → 7
# 5.  [-7] → -7
# 6.  [0,0,0] → 0
# 7.  [0,-1,0,-2] → 0
# 8.  [-1,-2,-3,-4] → -1
# 9.  [-5,-1,-8,-9] → -1
# 10. [1,-1,1,-1,1] → 1
# 11. [-2,3,-1,3,-2] → 5
# 12. [2,3,-1,4,5] → 13
# 13. [10,-20,30,-5,40] → 65
# 14. [-100,1,2,3,4] → 10
# 15. [-2,-3,4,-1,-2,1,5,-3] → 7
# 16. [0,-3,5,-2,0,3] → 6
# 17. [100000,-1,2,-1,3] → 100003
# 18. [-100000,100000] → 100000
# 19. [-2,-3,-1,-4] → -1
# 20. [1,-2,3,5,-3,2] → 8


def maximum_sum(nums):
    maxi=float('-inf')
    total=0
    for num in nums:
        total+=num
        maxi=max(maxi,total)
        if total<0:
            total=0
    return maxi

nums=list(map(int,input("Enter array elements : ").split()))
print(f"maximum subarray sum is : {maximum_sum(nums)}")