def largest_element(nums):
    if not nums:
        return None

    maxi = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > maxi:
            maxi = nums[i]
    return maxi


if __name__ == "__main__":
    nums = list(map(int, input().split()))
    result = largest_element(nums)
    if result is None:
        print("Empty array")
    else:
        print("Maximum value:", result)
