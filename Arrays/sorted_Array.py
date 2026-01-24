# ### Question

# **Given an array `nums`, determine whether it was originally sorted in non-decreasing order and then rotated some number of positions (including zero). The array may contain duplicates. Return `true` if possible, otherwise return `false`.**

# ---

# ### Intuition (Theory Only)

# A non-decreasing sorted array has a simple property:
# **every element is less than or equal to the next one**.

# When such an array is rotated:

# * The relative order of elements is preserved.
# * The array is still “almost sorted”.
# * The only place where the order can break is **at the rotation point**.

# That means:

# * The condition `nums[i] > nums[i+1]` can happen **at most once**.
# * Zero breaks → array was never rotated (already sorted).
# * One break → valid rotation point.
# * More than one break → impossible to form by a single rotation.

# Because rotation connects the **last element back to the first**, the array must be treated as **circular**. So the comparison between the last and first elements is just as important as internal comparisons.

# Duplicates do not affect this logic, because equality (`=`) is allowed in a non-decreasing order; only **strict decreases** matter.

# ---

# ### Key Takeaway

# > A rotated non-decreasing array can have **at most one place** where the order decreases when viewed circularly.



def check(nums):
    n=len(nums)
    drop=0
    for i in range(n):
        if nums[i]>nums[(i+1)%n]:
            drop+=1
            if drop > 1:
                return False
    return True
            

test_cases = [
    [1],                    # True  (single element)

    [1, 2],                 # True  (already sorted)
    [2, 1],                 # True  (rotated once)

    [1, 2, 3],              # True  (no rotation)
    [1, 2, 3, 4, 5],        # True
    [1, 1, 2, 2, 3],        # True  (duplicates allowed)

    [3, 4, 5, 1, 2],        # True  (valid rotation)
    [2, 3, 4, 5, 1],        # True
    [5, 1, 2, 3, 4],        # True

    [2, 2, 3, 1, 2],        # True  (rotation with duplicates)
    [3, 3, 1, 2, 3],        # True
    [1, 1, 1, 0, 1],        # True

    [2, 2, 2, 2],           # True  (all elements same)

    [3, 1, 4, 2],           # False (multiple drops)
    [4, 1, 3, 2],           # False

    [2, 1, 3, 4],           # False (cannot form sorted rotation)
    [1, 4, 2, 3],           # False

    [5, 4, 3, 2, 1],        # False (strictly decreasing)

    [1, 2, 3, 0],           # True  (single circular drop)

    [1, 3, 3, 2, 3],        # False (duplicate confusion)
    [2, 1, 1, 2, 1],        # False

    [100],                  # True  (boundary value)
    [100, 1],               # True  (valid rotation)

    [98, 99, 100, 1, 2],    # True

    [1, 2, 5, 3, 4],        # False
    [1, 3, 2],              # False

    [0, 0, 1, 1, 0],        # True
    [2, 3, 3, 3, 1, 2]      # True
]

for i in range(len(test_cases)):
    print(check(test_cases[i]))