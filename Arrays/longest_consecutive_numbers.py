# ## **Problem — Longest Consecutive Sequence**

# **Given:**
# An unsorted integer array `nums`.

# **Task:**
# Return the **length of the longest sequence of consecutive integers**.
# The sequence elements **do not need to be adjacent** in the array.

# ---

# ### **Example**

# | Input               | Output                          |
# | ------------------- | ------------------------------- |
# | `[100,4,200,1,3,2]` | `4`                             |
# | Explanation         | Longest sequence is `[1,2,3,4]` |

# ---

# ## **Professional Intuition**

# Brute force (sorting) costs **O(n log n)**.
# We can do better using a **Hash Set**.

# ### **Key Insight**

# A number starts a consecutive sequence **only if the previous number is not present**.

# For example, in `{1,2,3,4}`:

# * `1` is a starting point (because `0` not present)
# * `2,3,4` are NOT starting points

# So we:

# ---

# ### **Step-by-step Approach**

# 1. Insert all elements into a **set** → O(1) lookup.
# 2. For each number:

#    * If `num - 1` is **not** in the set → this is the start of a sequence.
#    * Keep checking `num + 1, num + 2...` until sequence breaks.
# 3. Track the **maximum length**.

# ## **Complexity**

# | Metric  | Complexity          |
# | ------- | ------------------- |
# | Time    | **O(n)**            |
# | Space   | **O(n)** (hash set) |
# | Optimal | ✅ Best possible     |

# ---

# ## **Test Cases**

# | Input                   | Output | Reason                 |
# | ----------------------- | ------ | ---------------------- |
# | `[100,4,200,1,3,2]`     | `4`    | Normal case            |
# | `[0,3,7,2,5,8,4,6,0,1]` | `9`    | Large sequence         |
# | `[1,2,0,1]`             | `3`    | Duplicates             |
# | `[9]`                   | `1`    | Single element         |
# | `[]`                    | `0`    | Empty array            |
# | `[5,5,5]`               | `1`    | All same               |
# | `[-1,0,1,2]`            | `4`    | Negative to positive   |
# | `[10,30,20]`            | `1`    | No consecutive numbers |
# | `[1,2,3,5,6,7,9]`       | `3`    | Multiple sequences     |




def longest_sequence(nums):
    n=len(nums)
    if n==0:
        return 0
    
    longest=1
    st=set()
    
    for num in nums:
        st.add(num)
    for ele in st:
        
        if ele-1 not in st:
            cnt=1
            x=ele
            while x+1 in st:
                x=x+1
                cnt+=1
            longest=max(longest,cnt)
    return longest


nums=list(map(int,input("Enter array elements : ").split()))
print(f"longest consecutive sequence is : {longest_sequence(nums)}")