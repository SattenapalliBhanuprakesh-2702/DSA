# 📌 Question

# Given an array nums containing n distinct numbers taken from the range [0, n], find the missing number from the range.

# Constraints:

# Array length = n

# Numbers range from 0 to n

# Exactly one number is missing

# 🧠 Intuition

# The sum of all numbers from 0 to n is known:

# ​total=int((n*(n+1))/2)

# Compute the sum of array elements.

# Subtract the array sum from the total sum → the missing number.

# Why it works:

# The difference between the expected sum and actual sum is exactly the missing number since only one number is missing.

# Alternative (XOR-based) intuition:

# XOR all numbers from 0 to n and XOR all array elements.

# XOR of these two gives the missing number.

# Works because a ^ a = 0 and a ^ 0 = a.

# ⏱️ Complexity
# Metric	Value
# Time Complexity	O(n) → single pass through the array
# Space Complexity	O(1) → only integer variables used
# Optimality	Yes, cannot do better than O(n) in single-pass
# Alternative	XOR solution: O(n) time, O(1) space, avoids sum overflow
# 🧪 Test Cases (Covering All Edge Cases)
# [
#     # 1. Missing number in the middle
#     {"input": [3, 0, 1], "output": 2},

#     # 2. Missing number is n (last element)
#     {"input": [0, 1], "output": 2},

#     # 3. Missing number is 0 (first element)
#     {"input": [1, 2, 3], "output": 0},

#     # 4. Single-element array, missing 0
#     {"input": [1], "output": 0},

#     # 5. Single-element array, missing 1
#     {"input": [0], "output": 1},

#     # 6. Larger array, missing middle number
#     {"input": [0, 1, 2, 4, 5, 6], "output": 3},

#     # 7. Larger array, missing last number
#     {"input": [0, 1, 2, 3, 4, 5, 6, 7, 8], "output": 9},

#     # 8. Missing number in a shuffled array
#     {"input": [9, 6, 4, 2, 3, 5, 7, 0, 1], "output": 8},

#     # 9. Missing number is 0, shuffled array
#     {"input": [1, 2, 3, 4], "output": 0},

#     # 10. Array with maximum n = 100000 (performance)
#     {"input": list(range(100000)), "missing": 100000, "output": 100000}
# ]

# 🎯 Interview Explanation

# “I calculate the expected sum of numbers from 0 to n, subtract the sum of the array elements, and the difference gives the missing number. This approach is O(n) in time and O(1) in space. Alternative XOR-based solution works too.”

# This is fully interview-ready, covers all edge cases, and explains intuition, complexity, and test cases in one place.

def missing_number(nums):
    n=len(nums)
    summation=0
    total=int((n*(n+1))/2.0)
    for i in range(n):
        summation+=nums[i]
    return total-summation

nums=list(map(int,input().split(" ")))
print(missing_number(nums))



# Another optimal solution using XOR based
# def missing_number(nums):
#     n = len(nums)
#     xor_total = 0
#     xor_array = 0
    
#     for i in range(n + 1):
#         xor_total ^= i
    
#     for num in nums:
#         xor_array ^= num
    
#     return xor_total ^ xor_array

# # Example usage:
# nums = list(map(int, input().split()))
# print(missing_number(nums))
