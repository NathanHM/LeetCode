nums = [0]
val = 1


def removeElement(nums, val):

        i = 0
        j = len(nums) - 1

        for _ in range(len(nums)):
            while i < len(nums) - 1 and nums[i] != val:
                i += 1
            while nums[j] == val and j >= 0:
                j -= 1
            if nums[j] != val and nums[i] == val and i < j:
                nums[i] = nums[j]
                nums[j] = val

        return j + 1


k = removeElement(nums, val)
print(nums)
print(k)
