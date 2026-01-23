def second_largest(nums):
   
    if len(nums) < 2:
        return None
    
    largest=float('-inf')
    second=float('-inf')

    for ele in nums:
        if ele > largest:
            second=largest
            largest=ele
        elif ele < largest and ele > second:
            second=ele
    return None if second==float('-inf') else second

if __name__=="__main__":
    nums = list(map(int, input().split()))
    second_larger=second_largest(nums)
    if second_larger:
        print("second largest element :",second_larger)
    else:
        print("Array is Empty")