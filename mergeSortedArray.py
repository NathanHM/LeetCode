nums1 = [4, 5, 6, 0, 0, 0]
m = 3
nums2 = [1, 2, 3]
n = 3


def newMergeSorted(nums1, nums2, m, n):

    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p >= 0 and p2 != -1:
        if nums2[p2] <= nums1[p1]:
            if p1 == -1:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1


newMergeSorted(nums1, nums2, m, n)

print(nums1)
