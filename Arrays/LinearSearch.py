
def LinearSearch(nums,ele):
    n=len(nums)
    for i in range(n):
        if nums[i]==ele:
            return i
    return -1


nums=list(map(int,input().split(" ")))
ele=int(input("Enter search element :"))
print(LinearSearch(nums,ele))