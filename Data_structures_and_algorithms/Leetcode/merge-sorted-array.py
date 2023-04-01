def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = 0
    j = 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            i += 1
        else:
            nums1.insert(i, nums2[j])
            nums1.pop()
            j += 1
            m += 1
    if j < n:
        nums1[m:] = nums2[j:]

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

merge(nums1, 3, nums2, 3)
print(nums1)
