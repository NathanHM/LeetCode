nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


def mergeSorted(nums1, nums2, m, n):

    i = 0

    # edge case: If nums1 is empty and nums2 is not, then swap
    # all values in nums1 for values in nums 2
    if m == 0 and n > 0:
        for index in range(n):
            nums1[index] = nums2[index]
        return
    # edge case: If nums2 is empty, do not change nums1
    elif n == 0:
        return
    else:
        # Iterate through nums 1
        for j in range(m + n):
            # if nums2 has a lower value in it's first postion, swap 
            # it for the present value in nums2
            if nums2[i] < nums1[j]:
                proxy = nums1[j]
                nums1[j] = nums2[i]
                nums2[i] = proxy
                del proxy
            # once past all the numbers present in nums1, swap for 
            # values in nums2
            if j >= m:
                nums1[j] = nums2[i]
                i += 1
        return


mergeSorted(nums1, nums2, m, n)

print(nums1)
