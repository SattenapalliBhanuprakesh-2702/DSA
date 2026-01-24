# ### Question

# **Given a sorted array `nums`, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements must be preserved. Return the array containing only the unique elements.**

# ---

# ### Intuition (Theory Only)

# Because the array is **sorted**, all duplicate values appear **next to each other**. This property allows us to avoid extra memory and nested loops.

# The idea is to maintain two logical regions in the array:

# * A **confirmed unique region** at the beginning
# * An **unprocessed region** that we scan through

# One pointer tracks the **last unique element**.
# Another pointer moves forward to inspect each new element.

# Whenever a new element differs from the last unique one, it is a **new unique value** and is placed immediately after the unique region. Duplicates are simply skipped.

# By doing this in a single pass:

# * All unique elements are compacted at the front
# * Order is preserved
# * No additional space is required

# Only the prefix of the array containing the unique elements is considered valid; elements beyond that are irrelevant.

# ---

# ### Key Takeaway

# > In a sorted array, duplicates cluster together, so a two-pointer scan is enough to overwrite duplicates in-place and keep only unique elements in linear time.

def Remove_duplicates(nums):
    i,j=0,1
    n=len(nums)
    while j<n:
        if nums[i]!=nums[j]:
            nums[i+1]=nums[j]
            i+=1
        j+=1
    return nums[:i+1]

nums=[1,1,1,2,2,3,3,3]
print(Remove_duplicates(nums))



#testcases
# test_cases = [
#     [],                         # Edge case: empty array → []
#     [5],                        # Single element → [5]
#     [2, 2],                     # Two same elements → [2]
#     [2, 3],                     # Two different elements → [2, 3]
#     [1, 1, 1, 1],               # All elements same → [1]
#     [1, 2, 3, 4, 5],            # Already unique → [1, 2, 3, 4, 5]
#     [1, 1, 2, 2, 3, 3],         # Alternating duplicates → [1, 2, 3]
#     [1, 1, 1, 2, 2, 3, 3, 3],   # Normal mixed case → [1, 2, 3]
#     [-5, -5, -3, -3, -1, 0],    # Negative numbers with duplicates → [-5, -3, -1, 0]
#     [0, 0, 0, 1, 1, 2],         # Zero-heavy array → [0, 1, 2]
#     [1, 1, 1, 1, 2],            # Duplicates at start → [1, 2]
#     [1, 2, 2, 2, 2],            # Duplicates at end → [1, 2]
#     [1, 1, 2, 3, 4, 4],         # Duplicates at both ends → [1, 2, 3, 4]
# ]
