

def maximum_sum(nums):
    maxi=float('-inf')
    total=0
    for num in nums:
        total+=num
        maxi=max(maxi,total)
        if total<0:
            total=0
    return maxi

nums=list(map(int,input("Enter array elements : ").split()))
print(f"maximum subarray sum is : {maximum_sum(nums)}")