# ## **Problem — Next Permutation**

# **Given:**
# An integer array `nums` representing a permutation of numbers.

# **Task:**
# Rearrange the numbers into the **lexicographically next greater permutation**.

# * If such arrangement is not possible (array is in descending order), rearrange it to the **lowest possible order** (ascending).
# * The modification must be **in-place** and use **O(1) extra space**.

# ---

# ### **Example**

# | Input     | Output    |
# | --------- | --------- |
# | `[1,2,3]` | `[1,3,2]` |
# | `[3,2,1]` | `[1,2,3]` |
# | `[1,1,5]` | `[1,5,1]` |

# ---

# ## **Professional Intuition**

# This problem is about finding the **next bigger number using the same digits**.

# ### **Key Insight**

# A permutation increases lexicographically from **right to left**.

# We follow **3 core steps**:

# ---

# ### **Step 1 — Find the Breakpoint**

# Traverse from right to left to find the first index `i` such that:

# ```
# nums[i] < nums[i + 1]
# ```

# This is the point where the increasing order from the right **breaks**.

# * If no such index exists → the array is in descending order (largest permutation).
#   → Reverse the array to get the smallest permutation.

# ---

# ### **Step 2 — Find Next Greater Element**

# From the right side again, find the **smallest element greater than `nums[i]`**, and swap them.

# Why?
# We want the **next immediate greater** permutation, not a large jump.

# ---

# ### **Step 3 — Reverse the Right Half**

# After swapping, the right side is still in **descending order**.
# Reverse it to make it **ascending**, giving the **smallest possible suffix**.

# ---

# ### **Why This Works**

# We change the number **just slightly bigger** than the current one by:

# * Increasing the number at the first possible position (from right)
# * Minimizing the rest of the digits

# This guarantees the **next lexicographic permutation**, not just a bigger one.

# ---

# ## **Complexity Analysis**

# | Metric  | Complexity              |
# | ------- | ----------------------- |
# | Time    | **O(n)** — max 3 passes |
# | Space   | **O(1)** — in-place     |
# | Optimal | ✅ Yes                   |

# ---

# ## **Test Cases**

# | Input           | Output          | Reason                      |
# | --------------- | --------------- | --------------------------- |
# | `[1,2,3]`       | `[1,3,2]`       | Normal case                 |
# | `[3,2,1]`       | `[1,2,3]`       | Highest permutation → reset |
# | `[1,1,5]`       | `[1,5,1]`       | Duplicates                  |
# | `[1,3,2]`       | `[2,1,3]`       | Middle case                 |
# | `[2,3,1]`       | `[3,1,2]`       | Pivot in middle             |
# | `[1]`           | `[1]`           | Single element              |
# | `[1,5,1]`       | `[5,1,1]`       | Duplicate pivot             |
# | `[5,4,7,5,3,2]` | `[5,5,2,3,4,7]` | Complex swap                |
# | `[2,2,0,4,3,1]` | `[2,2,1,0,3,4]` | Multiple reversals          |




def next_permutation(nums):
    n=len(nums)
    index=-1
    for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            index=i
            break
    if index==-1:
        nums.reverse()
        return
    
    for i in range(n-1,index,-1):
        if nums[i]>nums[index]:
            nums[index],nums[i]=nums[i],nums[index]
            break
    nums[index+1:]=reversed(nums[index+1:])
    
    return

nums=list(map(int,input("Enter the array elements : ").split()))
next_permutation(nums)
print("Next greater permutation :",nums)
