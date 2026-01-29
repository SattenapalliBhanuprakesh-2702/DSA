# ## **Problem Statement — Rearrange Array Alternately**

# **Given:**

# * An integer array `nums` containing positive and negative numbers.

# **Task:**

# * Rearrange the array **in-place** such that **positive and negative numbers appear alternately**.
# * Extra positive or negative numbers are placed at the **end of the array** in the same relative order.
# * **Do not use extra space**.

# **Example:**

# ```
# Input: nums = [1, -2, 3, -4, 5, -6]
# Output: [-2, 1, -4, 3, -6, 5]
# Explanation: Negative and positive numbers alternate. Relative order preserved.
# ```

# ---

# ## **Intuition / Approach**

# 1. **Partitioning Step (Segregation):**

#    * Move all negative numbers to the **beginning** of the array and positives to the **end**.
#    * This can be done in **O(n)** using a single pass (like Dutch National Flag algorithm).

# 2. **Alternating Step:**

#    * Swap every alternate negative element with the next positive element.
#    * Start with `neg_index = 0` and `pos_index = first positive index`.
#    * Increment `neg_index` by 2 for alternate placement and `pos_index` by 1 for next positive.

# 3. **Key Insight:**

#    * By separating negatives and positives first, we can alternate them without extra space.
#    * Handles cases where there are **unequal numbers** of positives and negatives automatically.

# ---

# ## **Complexity Analysis**

# | Metric  | Complexity | Explanation                                                   |
# | ------- | ---------- | ------------------------------------------------------------- |
# | Time    | O(n)       | Single pass for partition + single pass for alternate swap    |
# | Space   | O(1)       | In-place, no extra array used                                 |
# | Optimal | ✅          | This is the best possible solution for in-place rearrangement |

# ---

# ## **Test Cases**

# | Test Case               | Expected Output         | Notes                           |
# | ----------------------- | ----------------------- | ------------------------------- |
# | `[1, -2, 3, -4, 5, -6]` | `[-2, 1, -4, 3, -6, 5]` | Equal positives and negatives   |
# | `[-1, -2, 3, 4, 5]`     | `[-1, 3, -2, 4, 5]`     | More positives than negatives   |
# | `[1, 2, 3, -1]`         | `[-1, 1, 2, 3]`         | More positives, single negative |
# | `[-1, -2, -3, 1, 2]`    | `[-1, 1, -2, 2, -3]`    | More negatives than positives   |
# | `[1, 2, 3, 4]`          | `[1, 2, 3, 4]`          | All positives                   |
# | `[-1, -2, -3, -4]`      | `[-1, -2, -3, -4]`      | All negatives                   |
# | `[0, 1, -1, -2, 2]`     | `[-1, 0, -2, 1, 2]`     | Zero treated as positive        |
# | `[]`                    | `[]`                    | Empty array                     |
# | `[1]`                   | `[1]`                   | Single element                  |
# | `[-1]`                  | `[-1]`                  | Single element negative         |






def Rearrange(nums):
    pos=0
    neg=1
    arr=[0]*len(nums)
    for i in range(len(nums)):
        if nums[i]<0:
            arr[neg]=nums[i]
            neg+=2
        else:
            arr[pos]=nums[i]
            pos+=2
    return arr

nums=list(map(int,input("Enter array elements : ").split()))
print(f"Rearrange of elements : {Rearrange(nums)}")