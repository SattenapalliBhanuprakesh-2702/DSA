# 📌 Question
# Given an array nums where every element appears exactly twice except for one element that appears only once, find that single element.

# Example:

# Input: [1,3,5,5,1]
# Output: 3
# Explanation: 3 appears only once; all other numbers appear twice.

# 🧠 Intuition

# Use XOR properties:

# a ^ a = 0 → duplicates cancel out

# a ^ 0 = a → XOR with zero returns the number

# XOR all elements in the array:

# All numbers appearing twice cancel out to 0

# The remaining number is the one that appears once

# Why it works:

# XOR is associative and commutative, so order doesn’t matter.

# Efficiently finds the unique element without extra memory or sorting.

# ⏱️ Complexity
# Metric	Value
# Time Complexity	O(n) → single pass through array
# Space Complexity	O(1) → only one variable (xor) used
# Optimality	✅ Linear time, constant space — optimal

# 🧪 Test Cases (Covering All Edge Cases)
# [
#     # 1. Unique element in the middle
#     {"input": [1,3,5,5,1], "output": 3},

#     # 2. Unique element at the start
#     {"input": [7,1,1,3,3], "output": 7},

#     # 3. Unique element at the end
#     {"input": [2,2,4,4,9], "output": 9},

#     # 4. Only one element
#     {"input": [10], "output": 10},

#     # 5. Larger array with multiple duplicates
#     {"input": [1,2,3,2,1,4,4], "output": 3},

#     # 6. Negative numbers
#     {"input": [-1,-2,-2,-3,-1], "output": -3},

#     # 7. Mixed negative and positive
#     {"input": [-1,2,2,-3,-1], "output": -3},
# ]

# 🎯 Interview Explanation

# “I XOR all numbers in the array. Because XOR cancels duplicates, the remaining number is the one that appears only once. This is O(n) in time and O(1) in space, optimal and handles all edge cases including negative numbers.”


def Appear_onces(nums):
    xor=0
    for num in nums:
        xor ^=num
    return xor

nums=[1,3,5,5,1]
print(Appear_onces(nums))