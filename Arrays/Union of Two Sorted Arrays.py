# Below is **everything in one place**, clean, structured, and **interview-ready**, based **exactly on your code and intuition**.

# ---

# ## 📌 Question

# **Given two sorted integer arrays `nums1` and `nums2`, possibly containing duplicate elements, return a sorted array representing the union of the two arrays.**

# ### Conditions:

# * The result should contain **only unique elements**
# * The output must be **sorted**
# * Both input arrays are already sorted
# * Elements may repeat within and across arrays

# ---

# ## 🧠 Your Intuition (Explained Clearly)

# Your approach follows the **merge logic of merge sort**, enhanced with **duplicate elimination**.

# ### Key ideas behind your solution:

# * Use **two pointers** (`i` and `j`) to traverse both arrays
# * Always compare current elements:

#   * Pick the **smaller element**
#   * If both are equal, pick it **only once**
# * To avoid duplicates:

#   * Add an element to the result **only if it is different from the last inserted element**
# * After one array finishes:

#   * Append remaining unique elements from the other array

# This guarantees:

# * Sorted order
# * No duplicates
# * No unnecessary comparisons

# ---

# ## ⏱️ Complexity Analysis

# | Type                 | Value                     |
# | -------------------- | ------------------------- |
# | **Time Complexity**  | `O(n + m)`                |
# | **Space Complexity** | `O(n + m)` (output array) |
# | **Extra Space**      | No extra data structures  |

# This is the **optimal solution** for sorted arrays.

# ---

# ## 🧪 All Test Cases (Including Edge Cases)

# ### 1️⃣ Both arrays empty

# ```
# Input:
# nums1 = []
# nums2 = []

# Output:
# []
# ```

# ---

# ### 2️⃣ First array empty

# ```
# Input:
# nums1 = []
# nums2 = [1, 1, 2, 3]

# Output:
# [1, 2, 3]
# ```

# ---

# ### 3️⃣ Second array empty

# ```
# Input:
# nums1 = [1, 2, 3]
# nums2 = []

# Output:
# [1, 2, 3]
# ```
# ## 🎯 Interview Closing Statement

# > “I use a two-pointer merge approach on sorted arrays, ensuring uniqueness by comparing with the last inserted element. This achieves linear time complexity and handles all edge cases efficiently.”

# This explanation is **100% aligned with FAANG / product-company interview expectations**.


def union_of_arrays(nums1,nums2,n,m):
    res=[]
    i=j=0
    if n==m==0:
        return []
    while i<n and j<m:
        if nums1[i]<nums2[j]:
            if not res or nums1[i]!=res[-1]:
                res.append(nums1[i])
            i+=1
                
        elif nums1[i]==nums2[j]:
            if not res or nums1[i]!=res[-1]:
                res.append(nums1[i])
            i+=1
            j+=1
        
        else:
            if not res or nums2[j]!=res[-1]:
                res.append(nums2[j])
            j+=1
                
    while i<n:
        if not res or nums1[i]!=res[-1]:
            res.append(nums1[i])
        i+=1
        
    while j<m:
        if not res or nums2[j]!=res[-1]:
            res.append(nums2[j])
        j+=1
        
    return res



if __name__=="__main__":
    nums1=list(map(int,input().split(" ")))
    nums2=list(map(int,input().split(" ")))
    print(union_of_arrays(nums1,nums2,len(nums1),len(nums2)))