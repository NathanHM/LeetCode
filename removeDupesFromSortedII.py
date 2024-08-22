nums = [0,0,1,1,1,1,2,3,3]


def removeDuplicates(nums):

    j = 0
    echo = 0

    for i in range(1, len(nums)):

        if j == echo and nums[i] == nums[j]:
            j += 1
            nums[j] = nums[echo]

        if nums[i] != nums[j] and nums[i] != nums[echo]:
            j += 1
            echo = j
            nums[j] = nums[i]

    return j + 1


print(nums)
k = removeDuplicates(nums)
print(nums)
print(k)
