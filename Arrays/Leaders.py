# ## **Problem Statement — Leaders in an Array**

# **Given:**

# * An integer array `nums` of size `n`.

# **Task:**

# * An element is called a **leader** if it is **strictly greater than all elements to its right**.
# * Find all **leaders** in the array in **order of appearance**.

# **Example:**

# ```
# Input: nums = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# Explanation: 
# - 17 > 4,3,5,2 → leader
# - 5 > 2 → leader
# - 2 → leader (last element is always a leader)
# ```

# ---

# ## **Intuition / Approach**

# 1. **Start from the rightmost element:**

#    * The **last element** is always a leader.

# 2. **Keep track of current maximum on the right:**

#    * Initialize `max_from_right = nums[-1]`
#    * Traverse array from **second last element to the first**:

#      * If `nums[i] > max_from_right`, it is a leader → add to the list.
#      * Update `max_from_right` to `nums[i]` if it is a leader.

# 3. **Reverse the leaders list at the end**:

#    * Because we traversed from the end, leaders are stored in **reverse order**.

# **Key Insight:**

# * By traversing from right to left and tracking the maximum seen so far, we can find leaders **in a single pass**.

# ---

# ## **Complexity Analysis**

# | Metric  | Complexity | Explanation                                                                |
# | ------- | ---------- | -------------------------------------------------------------------------- |
# | Time    | O(n)       | Single traversal of the array                                              |
# | Space   | O(n)       | List to store leaders                                                      |
# | Optimal | ✅          | Best solution using O(n) time, cannot do better than O(n) for this problem |

# ---

# ## **Test Cases**

# | Test Case              | Expected Output   | Notes                                          |
# | ---------------------- | ----------------- | ---------------------------------------------- |
# | `[16, 17, 4, 3, 5, 2]` | `[17, 5, 2]`      | Normal case                                    |
# | `[1, 2, 3, 4, 5]`      | `[5]`             | Increasing array → only last element is leader |
# | `[5, 4, 3, 2, 1]`      | `[5, 4, 3, 2, 1]` | Decreasing array → all elements are leaders    |
# | `[7, 10, 4, 10, 6, 5]` | `[10, 10, 6, 5]`  | Leaders may repeat if same value               |
# | `[1]`                  | `[1]`             | Single element → always leader                 |
# | `[]`                   | `[]`              | Empty array → no leaders                       |
# | `[2, 2, 2, 2]`         | `[2]`             | Equal elements → last element only             |




def Leaders_Array(nums):
    n=len(nums)
    leaders=[]
    leaders.append(nums[n-1])
    for i in range(n-2,-1,-1):
        if nums[i]>leaders[-1]:
            leaders.append(nums[i])
    l=len(leaders)
    for i in range(l//2):
        leaders[i],leaders[l-i-1]=leaders[l-i-1],leaders[i]
    return leaders

nums=list(map(int,input("Enter array elements : ").split()))
print(f"leadrs of the array is : {Leaders_Array(nums)}")
    