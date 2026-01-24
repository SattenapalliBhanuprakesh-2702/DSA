# ### Question

# **Given an integer array `nums` and a non-negative integer `k`, rotate the array to the right by `k` steps in-place.**

# * You must perform the rotation **without using extra space** (O(1) space).
# * Example:

#   * Input: `nums = [1,2,3,4,5,6,7], k = 3`
#   * Output: `[5,6,7,1,2,3,4]`

# ---

# ### Intuition (Theory Only)

# Rotating an array to the right by `k` steps can be visualized as **moving the last `k` elements to the front**, while keeping the rest in order.

# To do this **in-place**, we use the **reversal algorithm**:

# 1. **Reverse the first `n-k` elements** → the part that stays at the back gets flipped.
# 2. **Reverse the last `k` elements** → the part that will move to the front gets flipped.
# 3. **Reverse the entire array** → the array is now correctly rotated.

# **Why it works:**

# * Reversing the two chunks separately prepares the elements so that a final reversal of the whole array places them in the correct rotated positions.
# * No extra space is needed, and each element is moved at most twice → **O(n) time, O(1) space**.

# **Key Insight for Interviews:**

# > “Rotation can be achieved by reversing sections of the array: first the fixed part, then the rotating part, then the whole array. This efficiently shifts elements without extra memory.”

def Rotate(nums,start,end):
    while start<end:
        nums[start],nums[end]=nums[end],nums[start]
        start+=1
        end-=1
    
def Rotate_array(nums,k):
    n=len(nums)
    k=k%n
    if k==0:
        return
    Rotate(nums,0,n-k-1)
    Rotate(nums,n-k,n-1)
    Rotate(nums,0,n-1)
    
nums=[1,2,3,4,5,6]
k=3
Rotate_array(nums,k)
print(nums)