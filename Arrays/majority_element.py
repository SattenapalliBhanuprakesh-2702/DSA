# Here’s a **complete breakdown** of the Majority Element problem using the **Boyer-Moore Voting Algorithm**.

# ---

# ## **Question — Majority Element**

# **Problem Statement:**

# Given an array `nums` of size `n`, find the **majority element**—an element that occurs **more than n/2 times**.

# * If such an element exists → return it
# * Otherwise → return `None`

# **Constraints:**

# * 1 ≤ n ≤ 10^5
# * nums[i] can be **any integer** (positive, negative, zero)

# ---

# ## **Intuition (Boyer-Moore Voting Algorithm)**

# 1. A **majority element** is more than half of the array, so it **cannot be canceled out** by other elements.

# 2. Use **candidate + count**:

#    * Initialize `candidate = None`, `count = 0`.
#    * Traverse the array:

#      * If `count == 0` → choose the current element as `candidate`.
#      * If current element == `candidate` → increment `count`.
#      * Else → decrement `count`.

# 3. After traversal, `candidate` is the **potential majority**.

# 4. **Optional verification**: Count how many times `candidate` occurs. If > n/2 → return it; else → return `None`.

# ---

# ### **Step-by-Step Example**

# ```
# nums = [2,2,1,1,1,2,2]
# n = 7
# ```

# | Step | num | candidate | count |
# | ---- | --- | --------- | ----- |
# | 0    | 2   | 2         | 1     |
# | 1    | 2   | 2         | 2     |
# | 2    | 1   | 2         | 1     |
# | 3    | 1   | 2         | 0     |
# | 4    | 1   | 1         | 1     |
# | 5    | 2   | 1         | 0     |
# | 6    | 2   | 2         | 1     |

# * Candidate at the end → **2**
# * Count 2 → 4 times > 3.5 → **majority found**

# ---

# ## **Complexity**

# | Type    | Complexity                                                                   |
# | ------- | ---------------------------------------------------------------------------- |
# | Time    | **O(n)** → single pass for candidate + optional second pass for verification |
# | Space   | **O(1)** → constant space, no extra data structures                          |
# | Optimal | ✅ This is the most efficient solution                                        |

# ---

# ## **Test Cases (All Edge Cases)**

# ```
# 1. nums=[3,3,4] → 3                     # basic majority
# 2. nums=[2,2,1,1,1,2,2] → 2             # majority at end
# 3. nums=[1] → 1                          # single element
# 4. nums=[1,2] → None                     # no majority
# 5. nums=[1,1,2,2,2] → 2                  # majority in middle
# 6. nums=[0,0,0,0,0,1,2] → 0              # majority at start
# 7. nums=[-1,-1,-1,2,3] → -1              # negative numbers
# 8. nums=[5,5,5,5,5] → 5                  # all same elements
# 9. nums=[1,2,3,4,5,6] → None             # no majority
# 10. nums=[1,1,1,2,2,2,2] → 2             # tie but > n/2 check
# 11. nums=[1000000,-1000000,1000000] → 1000000 # large numbers
# 12. nums=[1,2,3,1,2,3,1] → 1             # majority in scattered positions
# 13. nums=[0,0,1,1,1,0,0] → 0             # zeros as majority
# 14. nums=[-5,-5,-5,-5,0,1] → -5          # negative majority
# 15. nums=[1,2,3,4,5,6,7,8,9,10] → None    # all distinct → no majority
# ```

# ---

# This covers:

# * Single element arrays
# * No majority
# * Positive, negative, zero
# * Large numbers
# * Scattered majority
# * All elements the same



def majority_element(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    
    
    if nums.count(candidate) > len(nums)//2:
        return candidate
    return None


nums = list(map(int, input("Enter array elements: ").split()))
print(majority_element(nums))
