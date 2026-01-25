# 📌 Question

# Given a binary array nums (containing only 0s and 1s), find the maximum number of consecutive 1s in the array.

# Example:

# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The longest sequence of 1s is [1,1,1].

# 🧠 Intuition

# Traverse the array once, keeping track of:

# count → current streak of consecutive 1s

# maxi → maximum streak found so far

# For each element:

# If it’s 1 → increment count and update maxi if needed

# If it’s 0 → reset count to 0

# By the end, maxi stores the length of the longest consecutive 1s sequence.

# Why it works:

# A single pass captures every consecutive sequence.

# Resetting at 0 ensures broken sequences do not carry over.

# ⏱️ Complexity
# Metric	Value
# Time Complexity	O(n) → single pass through array
# Space Complexity	O(1) → only counters used
# Optimality	✅ Linear time, constant space


# 🧪 Test Cases (Including Edge Cases)
# [
#     # 1. Normal case
#     {"input": [1,1,0,1,1,1], "output": 3},

#     # 2. All 1s
#     {"input": [1,1,1,1,1], "output": 5},

#     # 3. All 0s
#     {"input": [0,0,0], "output": 0},

#     # 4. Single element 1
#     {"input": [1], "output": 1},

#     # 5. Single element 0
#     {"input": [0], "output": 0},

#     # 6. Alternating 1s and 0s
#     {"input": [1,0,1,0,1,0,1], "output": 1},

#     # 7. Long consecutive 1s at the start
#     {"input": [1,1,1,0,0,1,0,1], "output": 3},

#     # 8. Long consecutive 1s at the end
#     {"input": [0,0,1,1,1,1], "output": 4},

#     # 9. Large array with random 0s and 1s
#     {"input": [1]*5000 + [0] + [1]*7000, "output": 7000},

#     # 10. Empty array
#     {"input": [], "output": 0}
# ]

# 🎯 Interview Explanation

# “I traverse the array once, maintaining a counter for the current streak of 1s and a variable for the maximum streak. Every 0 resets the counter. This is O(n) in time and O(1) in space, and handles all edge cases including empty arrays or arrays with only 0s or 1s.”

def consecutive_ones(nums):
    count = 0
    maxi = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            maxi = max(maxi, count)
            count = 0
    return max(maxi, count)  

nums = [1,1,0,1,1,1]
print(consecutive_ones(nums))

        