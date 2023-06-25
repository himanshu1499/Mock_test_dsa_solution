def moveZeroes(nums):
    nonZeroIndex = 0


    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nonZeroIndex] = nums[i]
            nonZeroIndex +=1

    # fill the remaining elements with zeros
    for i in range(nonZeroIndex,len(nums)):
        nums[i] = 0

    return nums
