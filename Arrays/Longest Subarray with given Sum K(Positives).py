# **Problem Statement**
# Given an array of **positive integers** `nums` and an integer `k`, return the **length of the longest contiguous subarray** whose sum equals `k`. If no such subarray exists, return `0`.

# ---

# ## Intuition Behind the Approach (Sliding Window)

# Because all numbers are **positive**, the window sum behaves predictably:

# * Expanding the window (move `right`) → sum **increases**
# * Shrinking the window (move `left`) → sum **decreases**

# This monotonic behavior allows a **two-pointer sliding window** instead of checking all subarrays.

# ### Strategy

# 1. Start with two pointers at the beginning.
# 2. Keep adding elements to the window.
# 3. If sum exceeds `k`, shrink from the left.
# 4. When sum equals `k`, update max length.
# 5. Continue scanning to find longer windows.

# This works **only for positive numbers**.

# ---

# ## Algorithm Logic

# * Maintain:

#   * `left` pointer
#   * running `sum`
#   * current window length
#   * maximum length found

# ---

# ## Time & Space Complexity

# | Metric           | Value                                         |
# | ---------------- | --------------------------------------------- |
# | Time Complexity  | **O(n)** (each element visited at most twice) |
# | Space Complexity | **O(1)**                                      |

# This is **optimal**.

# ---

# ## Edge Cases & Test Cases

# | #  | Input `nums`      | `k` | Expected Output | Reason                                |
# | -- | ----------------- | --- | --------------- | ------------------------------------- |
# | 1  | `[5,1,2,3]`       | 5   | **2**           | `[2,3]` longer than `[5]`             |
# | 2  | `[1,2,3,4,5]`     | 9   | **3**           | `[2,3,4]`                             |
# | 3  | `[1,1,1,1,1]`     | 3   | **3**           | multiple same numbers                 |
# | 4  | `[2,4,6]`         | 5   | **0**           | no subarray                           |
# | 5  | `[5]`             | 5   | **1**           | single element equals k               |
# | 6  | `[5]`             | 3   | **0**           | single element not equal              |
# | 7  | `[1,2,1,1,1,3]`   | 3   | **3**           | `[1,1,1]`                             |
# | 8  | `[3,3,3]`         | 3   | **1**           | many small windows                    |
# | 9  | `[1,2,3]`         | 6   | **3**           | entire array                          |
# | 10 | `[1,2,3]`         | 7   | **0**           | sum never reaches                     |
# | 11 | `[10,2,3]`        | 5   | **0**           | large first element                   |
# | 12 | `[]`              | 5   | **0**           | empty array                           |
# | 13 | `[1,4,1,1,1,2,3]` | 5   | **4**           | `[1,1,1,2]`                           |
# | 14 | `[2,2,2,2]`       | 4   | **2**           | repeated values                       |
# | 15 | `[1,3,1,1,1]`     | 5   | **4**           | `[3,1,1]` vs `[1,1,1,2]` pattern test |

# ---

# ## Important Interview Note

# This solution **fails if negative numbers exist** because the sum would no longer grow/shrink predictably.
# For arrays with negatives → use **prefix sum + hashmap (O(n))** instead.



def longest_subarray(nums,k):
    maxi=total=0
    left=count=0
    for right in range(len(nums)):
        total+=nums[right]
        
        if total > k:
            total-=nums[left]
            left+=1
            count-=1
        count+=1
        if total==k:
            if count>maxi:
                maxi=count
    return maxi


if __name__=="__main__":
    nums=list(map(int,input("Enter array elements : ").split()))
    k=int(input("Enter target value : "))
    print(longest_subarray(nums,k))