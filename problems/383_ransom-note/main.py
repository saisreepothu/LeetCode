class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = {}
        for i in magazine:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i]+=1
        for j in ransomNote:
            if j in hm and hm[j] != 0:
                hm[j]-=1
            else:
                return False
        return True


if __name__ == "__main__":
    samples = [
        {"ransomNote": "a", "magazine": "b", "expected": False},
        {"ransomNote": "aa", "magazine": "ab", "expected": False},
        {"ransomNote": "aa", "magazine": "aab", "expected": True},
    ]

    solver = Solution()
    for i, sample in enumerate(samples, start=1):
        result = solver.canConstruct(sample["ransomNote"], sample["magazine"])
        print(f"Sample {i} result: {result}")
        print(f"Sample {i} expected: {sample['expected']}")
