class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        s1 = s.lower()
        while i < j:
            if not s1[i].isalnum():
                i += 1
            elif not s1[j].isalnum():
                j -= 1
            else:
                if s1[i] != s1[j]:
                    return False
                i += 1
                j -= 1
        return True


if __name__ == "__main__":
    samples = [
        {"s": "A man, a plan, a canal: Panama", "expected": True},
        {"s": "race a car", "expected": False},
        {"s": " ", "expected": True},
    ]

    solver = Solution()
    for i, sample in enumerate(samples, start=1):
        result = solver.isPalindrome(sample["s"])
        print(f"Sample {i} result: {result}")
        print(f"Sample {i} expected: {sample['expected']}")
