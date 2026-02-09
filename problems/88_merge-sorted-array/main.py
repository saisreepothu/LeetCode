from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1
        while (i >= 0 and j >= 0):
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j-=1
                k-=1
            else:
                nums1[k] = nums1[i]
                i-=1
                k-=1
        while j >= 0:
            nums1[k] = nums2[j]
            j-=1
            k-=1
        return nums1


if __name__ == "__main__":
    samples = [
        {
            "nums1": [1, 2, 3, 0, 0, 0],
            "m": 3,
            "nums2": [2, 5, 6],
            "n": 3,
            "expected": [1, 2, 2, 3, 5, 6],
        },
        {
            "nums1": [1],
            "m": 1,
            "nums2": [],
            "n": 0,
            "expected": [1],
        },
        {
            "nums1": [0],
            "m": 0,
            "nums2": [1],
            "n": 1,
            "expected": [1],
        },
    ]

    solver = Solution()
    for i, sample in enumerate(samples, start=1):
        nums1 = sample["nums1"][:]
        nums2 = sample["nums2"][:]
        solver.merge(nums1, sample["m"], nums2, sample["n"])
        print(f"Sample {i} result: {nums1}")
        print(f"Sample {i} expected: {sample['expected']}")
