# Question

# Given an array nums, move all 0s to the end of the array while maintaining the relative order of the non-zero elements. The operation must be done in-place.

# Intuition (Theory Only)

# The key observation is that we only care about preserving the order of non-zero elements. Zeros have no ordering constraint relative to each other.

# Think of the array as having two logical parts:

# A front region where all non-zero elements should be compacted in order.

# A remaining region that will naturally end up containing zeros.

# We scan the array once from left to right.
# A pointer tracks the position where the next non-zero element should be placed.
# Whenever a non-zero element is encountered, it is swapped forward into the correct position.
# Zeros are skipped and automatically drift toward the end.

# This approach ensures:

# One pass over the array

# No extra space

# Order of non-zero elements is preserved

# All Test Cases (Including Edge Cases)
# Single list of test cases
# test_cases = [
#     [],                             # Empty array
#     [0],                            # Single zero
#     [5],                            # Single non-zero
#     [0, 0, 0],                      # All zeros
#     [1, 2, 3],                      # No zeros
#     [0, 1, 2, 3],                   # Zero at start
#     [1, 2, 3, 0],                   # Zero at end
#     [1, 0, 2, 3, 0],                # Zeros in middle
#     [0, 0, 1, 2, 3],                # Multiple zeros at start
#     [1, 2, 3, 0, 0],                # Multiple zeros at end
#     [1, 0, 2, 0, 3, 0, 4],           # Alternating zeros
#     [0, 1, 0, 3, 12],               # Common interview example
#     [-1, 0, -2, 0, 3],              # Negative numbers with zeros
#     [0, -1, 0, -2, 0, -3],          # Zeros and negatives mixed
#     [10, 0, 0, 20, 30, 0, 40],       # Large gaps with zeros
# ]

# Expected Output Pattern (Conceptual)

# For every test case:

# All non-zero elements stay in the same order

# All zeros move to the end

# Example:

# Input:  [1, 0, 2, 0, 3]
# Output: [1, 2, 3, 0, 0]

# Key Takeaway (Interview Line)

# By compacting non-zero elements forward using a pointer, zeros naturally shift to the end without extra space, achieving O(n) time and O(1) space.


def move_zeros_end(nums):
    n=len(nums)
    index=0
    for i in range(n):
        if nums[i]!=0:
            nums[index],nums[i]=nums[i],nums[index]
            index+=1
    return


nums=[1,0,2,0,3,0,4,0,5]
move_zeros_end(nums)
print(nums)