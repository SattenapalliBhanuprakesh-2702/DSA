# Question — Longest Subarray with Sum = Target

# Problem Statement:
# Given an integer array nums (can contain positive, negative, and zero) and an integer target, find the length of the longest contiguous subarray whose sum equals target.

# Return the length of that subarray.

# Algorithm
# First, we will declare a map to store the prefix sums and the indices.
# Then we will run a loop(say i) from index 0 to n-1(n = size of the array).
# For each index i, we will do the following:
# We will add the current element i.e. a[i] to the prefix sum.
# If the sum is equal to k, we should consider the length of the current subarray i.e. i+1. We will compare this length with the existing length and consider the maximum one.
# We will calculate the prefix sum i.e. x-k, of the remaining subarray.
# If that sum of the remaining part i.e. x-k exists in the map, we will calculate the length i.e. i-preSumMap[x-k], and consider the maximum one comparing it with the existing length we have achieved until now.
# If the sum, we got after step 3.1, does not exist in the map we will add that with the current index into the map. We are checking the map before insertion because we want the index to be as minimum as possible and so we will consider the earliest index where the sum x-k has occurred. [Detailed discussion in the edge case section]
# In this approach, we are using the concept of the prefix sum to solve this problem. Here, the prefix sum of a subarray ending at index i, simply means the sum of all the elements of that subarray.

# Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.

# Space Complexity: O(N) as we are using a map data structure.

# 1. nums=[1,-1,5,-2,3], target=3 → 4
# 2. nums=[-2,-1,2,1], target=1 → 2
# 3. nums=[1,2,3,4,5], target=11 → 3 ([3,4,5])
# 4. nums=[1,2,3,4,5], target=15 → 5 (whole array)
# 5. nums=[1,2,3,4,5], target=0 → 0 (no subarray)
# 6. nums=[3,1,2], target=3 → 1 ([3])
# 7. nums=[-1,-2,-3,-4], target=-6 → 3 ([-1,-2,-3])
# 8. nums=[0,0,0,0], target=0 → 4 (whole array)
# 9. nums=[5,1,2,3], target=5 → 2 ([5] or [2,3] depending on array sum positions)
# 10. nums=[1], target=1 → 1 (single element)
# 11. nums=[-1], target=1 → 0 (no subarray)
# 12. nums=[2, -2, 2, -2, 2], target=0 → 4 ([2,-2,2,-2])
# 13. nums=[1,2,-1,2,-1,2], target=3 → 5 ([2,-1,2,-1,2])
# 14. nums=[1000000,-1000000,1], target=1 → 2 ([-1000000, 1])


def longest_subarray(nums, target):
    seen = {0:-1}
    total = 0
    maxi = 0
    
    for i in range(len(nums)):
        total += nums[i]
        
        rem = total - target
        if rem in seen:
            length = i - seen[rem]
            maxi = max(maxi, length)
        
        if total not in seen:
            seen[total] = i
    return maxi

if __name__=="__main__":
    nums=list(map(int,input("Enter array element :").split()))
    target=int(input("Enter target value :"))
    print(longest_subarray(nums,target))
