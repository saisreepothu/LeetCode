from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_a = sorted(nums)
        ele = len(nums)//2
        return nums_a[ele]


if __name__ == "__main__":
    samples = [
        {"nums": [3, 2, 3], "expected": 3},
        {"nums": [2, 2, 1, 1, 1, 2, 2], "expected": 2},
    ]

    solver = Solution()
    for i, sample in enumerate(samples, start=1):
        result = solver.majorityElement(sample["nums"][:])
        print(f"Sample {i} result: {result}")
        print(f"Sample {i} expected: {sample['expected']}")
