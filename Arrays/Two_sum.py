# ### **Question — Two Sum**

# Given an integer array `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

# * Exactly **one solution** exists.
# * You **cannot use the same element twice**.
# * Order of indices does not matter.

# ---

# ## **Intuition**

# Instead of checking all pairs (which is slow), use **memory to trade for speed**.

# While scanning the array:

# 1. For each number `x`, compute `target - x` (the partner needed).
# 2. Check if that partner was already seen earlier.
# 3. If yes → solution found instantly.
# 4. If not → store current number with its index.

# This turns a double search into a **single-pass lookup problem**.

# Core idea:
# **"Find complement using hash lookup instead of nested loops."**

# ---

# ## **Complexity**

# | Type             | Value                       |
# | ---------------- | --------------------------- |
# | Time Complexity  | **O(n)**                    |
# | Space Complexity | **O(n)**                    |
# | Why optimal?     | Each element processed once |

# ---

# ## **All Important Test Cases (Including Edge Cases)**

# ```
# 1. nums=[2,7,11,15], target=9 → [0,1]              # basic
# 2. nums=[3,2,4], target=6 → [1,2]                 # unordered
# 3. nums=[3,3], target=6 → [0,1]                   # duplicates
# 4. nums=[1,5,1,5], target=10 → [1,3]              # repeating numbers
# 5. nums=[0,4,3,0], target=0 → [0,3]               # zeros
# 6. nums=[-1,-2,-3,-4,-5], target=-8 → [2,4]      # negatives
# 7. nums=[-3,4,3,90], target=0 → [0,2]            # mix pos/neg
# 8. nums=[1,2], target=3 → [0,1]                  # smallest valid array
# 9. nums=[5,75,25], target=100 → [1,2]            # large values
# 10. nums=[1000000, -1000000], target=0 → [0,1]   # extreme range
# 11. nums=[2,5,5,11], target=10 → [1,2]           # duplicate pair
# 12. nums=[1,2,3,4,4], target=8 → [3,4]           # pair at end
# 13. nums=[4,4,1,2,3], target=8 → [0,1]           # pair at start
# 14. nums=[-10,20,10,-20], target=0 → [0,2] or [1,3]
# 15. nums=[0,0,3,4], target=0 → [0,1]             # both zeros
# ```

# ---

# ## **Interview Summary**

# * Brute force = O(n²) ❌
# * Sorting + two pointers = loses indices ❌
# * **Hash map = industry standard solution** ✅


def two_sum(nums,k):
    seen={}
    for i,num in enumerate(nums):
        diff=k-num
        if diff in seen:
            return (seen[diff],i)
        seen[num]=i
            
if __name__=="__main__":
    nums=list(map(int,input().split()))
    k=int(input("Enter the target value :"))
    print(two_sum(nums,k))