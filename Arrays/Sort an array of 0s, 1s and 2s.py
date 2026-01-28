# This is a classic **Dutch National Flag problem** implementation. Here’s the full breakdown for interviews:

# ---

# ## **Question**

# **Problem Statement:**

# Given an array `nums` containing only `0`, `1`, and `2`, sort the array **in-place** so that all `0`s come first, followed by `1`s, then `2`s.

# You must **not** use a sorting function; aim for **O(n) time** and **O(1) space**.

# **Example 1:**

# ```
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# ```

# **Example 2:**

# ```
# Input: nums = [0]
# Output: [0]
# ```

# **Constraints:**

# * 1 ≤ nums.length ≤ 10^5
# * nums[i] ∈ {0,1,2}

# ---

# ## **Intuition**

# We use **three pointers** (`low`, `mid`, `high`) to partition the array:

# 1. **`low`** → next position for `0`
# 2. **`mid`** → current element being examined
# 3. **`high`** → next position for `2`

# Rules:

# * If `nums[mid] == 0`: swap with `nums[low]`, move `low` and `mid` forward.
# * If `nums[mid] == 1`: already in correct place, just move `mid` forward.
# * If `nums[mid] == 2`: swap with `nums[high]`, move `high` backward (don’t move `mid` because new element at `mid` must be checked).

# This guarantees **single pass** and **in-place** sorting.

# ---

# ## **Complexity**

# | Aspect  | Value                                      |
# | ------- | ------------------------------------------ |
# | Time    | O(n) → each element processed at most once |
# | Space   | O(1) → in-place                            |
# | Optimal | Yes                                        |

# ---

# ## **Test Cases (including edge cases)**

# ```
# 1. nums=[2,0,2,1,1,0] → [0,0,1,1,2,2]   # normal mix
# 2. nums=[0,0,0] → [0,0,0]               # all zeros
# 3. nums=[2,2,2] → [2,2,2]               # all twos
# 4. nums=[1,1,1] → [1,1,1]               # all ones
# 5. nums=[0,1,2] → [0,1,2]               # already sorted
# 6. nums=[2,1,0] → [0,1,2]               # reverse sorted
# 7. nums=[0,2,1,2,0,1,2] → [0,0,1,1,2,2,2] # large random
# 8. nums=[0] → [0]                        # single element
# 9. nums=[2] → [2]                        # single element
# 10. nums=[1] → [1]                        # single element
# 11. nums=[0,2,0,2,0,2] → [0,0,0,2,2,2]  # alternating 0 and 2
# 12. nums=[1,0,2,1,0,2,1] → [0,0,1,1,1,2,2] # mix with many 1s



def Sort_array(nums):
    n=len(nums)
    low=mid=0
    high=n-1
    while mid<=high:
        if nums[mid]==0:
            nums[mid],nums[low]=nums[low],nums[mid]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return

nums=list(map(int,input("Enter array element(only 0,1,2) : ").split()))
Sort_array(nums)
print(nums)