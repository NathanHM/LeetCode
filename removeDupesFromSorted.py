nums = [1,2,2]

def removeDuplicates(nums):
    
        j = 0
        
        for i in range(1, len(nums)):
              
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1
              


k = removeDuplicates(nums)
print(nums)
print(k)