target = 15
nums = [5,1,3,5,10,7,4,9,2,8]

def minSubarraySum (target, nums):


    subarray = []
    output = 0

    for i in range(len(nums)):

        subarray.append(nums[i])

        if sum(subarray) >= target:
            if sum(subarray) < output or output == 0:
                output = len(subarray)

            for j in range(1, len(subarray)):

                if sum(subarray[j:]) < target:
                    break

                elif len(subarray[j:]) < output:
                    output = len(subarray[j:])

            subarray = subarray[-output:]

    return output

def minSubarraySumII(target, nums):
    total = 0
    pointer = 0
    output = 0

    for i in range(len(nums)):
        total += nums[i]
        
        if total >= target:

            if (i + 1 - pointer) < output or output == 0:
                output = i + 1 - pointer

            sub = 0
            for j in range(pointer, i):
                sub += nums[j]
                
                if total - sub < target:
                    break
                else:
                    total -= sub
                    sub = 0
                    pointer += 1
                    if (i + 1 - pointer) < output or output == 0:
                        output = i + 1 - pointer

    return output

def minSubarraySumIII(target, nums):
    total = 0
    pointer = 0
    output = len(nums) + 1

    for i in range(len(nums)):

        total += nums[i]
        
        while total >= target:

            output = min(output, i + 1 - pointer)
            pointer += 1
            total -= nums[pointer]

    if output > len(nums):
        return 0
    else: 
        return output

print(minSubarraySumIII(target, nums))